from re import finditer
import ChatTTS
import torch
import torchaudio
from typing import List
import argparse
from pydub import AudioSegment
from pydub.silence import split_on_silence

def advanced(texts: List[str]):
    chat = ChatTTS.Chat()
    #chat.load('huggingface',compile=True, force_redownload=False) # Set to True for better performance
    chat.load(compile=False) # Set to True for better performance

    ###################################
    # Sample a speaker from Gaussian.

    rand_spk = chat.sample_random_speaker()
    print(rand_spk) # save it for later timbre recovery

    params_infer_code = ChatTTS.Chat.InferCodeParams(
        spk_emb = rand_spk, # add sampled speaker
        temperature = .3,   # using custom temperature
        top_P = 0.7,        # top P decode
        top_K = 20,         # top K decode
    )

    ###################################
    # For sentence level manual control.

    # use oral_(0-9), laugh_(0-2), break_(0-7)
    # to generate special token in text to synthesize.
    params_refine_text = ChatTTS.Chat.RefineTextParams(
        prompt='[oral_2][laugh_0][break_6]',
    )

    wavs = chat.infer(
        texts,
        params_refine_text=params_refine_text,
        params_infer_code=params_infer_code,
    )
    return wavs

def massage_data(original_lines: List[str]) -> List[str]:
    lines: List[str] = []
    for line in original_lines:
        lines.extend(line.strip().split('。'))
    clean_lines = [s for s in lines if len(s)>0]
    print(clean_lines)
    return clean_lines


def main():
    parser = argparse.ArgumentParser(description='News To Speech')
    parser.add_argument('-f',"--news-file", help="Text file include news lines", type=str, default="news.txt")
    args = parser.parse_args()

    output_path = "output"
    # Read news
    news_lines: List[str] = []
    with open(args.news_file,"r") as f:
        news_lines = f.readlines()

    # Massage data
    final_lines = massage_data(news_lines)

    # Generate wav for every line
    wavs = advanced(final_lines)
    wav_count = len(wavs)
    for i in range(wav_count):
        torchaudio.save(f"{output_path}/output_{i}.wav", torch.from_numpy(wavs[i]).unsqueeze(0), 24000)

    # Merge wav
    combined_wav = AudioSegment.empty()
    for i in range(0,wav_count):
         combined_wav = combined_wav + AudioSegment.from_wav(f"{output_path}/output_{i}.wav")

    # Remove silence chunk
    audio_chunks = split_on_silence(combined_wav, min_silence_len = 200, silence_thresh = -45, keep_silence = 100)
    final_wav = AudioSegment.empty()
    for chunk in audio_chunks:
        final_wav += chunk

    output_audio = f"{output_path}/output.mp3"
    final_wav.export(output_audio, format="mp3")

    print("=================================")
    print(f"Output: {output_audio}")
    print("=================================")

if __name__ == "__main__":
    main()
