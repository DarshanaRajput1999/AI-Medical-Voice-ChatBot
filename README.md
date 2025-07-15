# AI-Medical-Voice-ChatBot
An intelligent, voice-enabled medical chatbot that listens to the user, analyzes uploaded medical images, and responds in a natural-sounding voice—mimicking a real doctor. Built with OpenAI, ElevenLabs/gTTS, Whisper, and Gradio.

## 📌 Features

- 🎙️ **Speech-to-Text**: Captures patient input via voice using Whisper via Groq API.
- 🧠 **Medical Image Analysis**: Uses LLMs (like LLaMA-4) to analyze X-rays, rashes, or skin conditions.
- 💬 **Natural Language Generation**: Responds like a real doctor with concise, human-like explanations.
- 🔊 **Text-to-Speech**: Speaks back using ElevenLabs or gTTS.
- 🌐 **User-Friendly Gradio Interface**: Upload voice + image and get audio/text output instantly.

---

## 🛠️ Tech Stack

| Component       | Technology           |
|----------------|----------------------|
| Speech-to-Text | Whisper (via Groq)   |
| LLM for Query  | Meta LLaMA-4         |
| TTS            | ElevenLabs / gTTS    |
| Frontend       | Gradio               |
| Language       | Python               |

---

## 🔮 Future Improvements

- Add multilingual support (Hindi, Spanish, etc.)
- Enable real-time webcam image input
- HIPAA-compliant data storage
- Chat history and EMR integration
