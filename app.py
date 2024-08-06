import gradio as gr
import numpy as np
from transformers import pipeline

transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-base.en")
def transcribe(audio):
    sr, y = audio
    y = y.astype(np.float32)
    y /= np.max(np.abs(y))

    return transcriber({"sampling_rate": sr, "raw": y})["text"]  # type: ignore


with gr.Blocks() as demo:
  audio_input = gr.Audio(sources=["microphone"])
  transcription_output = gr.Textbox(lines=5)
  submit_button = gr.Button("Transcribe")

  submit_button.click(fn=transcribe, inputs=audio_input, outputs=transcription_output)

demo.launch()
