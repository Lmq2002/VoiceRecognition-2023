import wave

import numpy as np
import sherpa_ncnn as ncnn

def main():
    recognizer = ncnn.Recognizer(
        tokens="./sherpa-ncnn-conv-emformer-transducer-2022-12-06/tokens.txt",
        encoder_param="./sherpa-ncnn-conv-emformer-transducer-2022-12-06/encoder_jit_trace-pnnx.ncnn.param",
        encoder_bin="./sherpa-ncnn-conv-emformer-transducer-2022-12-06/encoder_jit_trace-pnnx.ncnn.bin",
        decoder_param="./sherpa-ncnn-conv-emformer-transducer-2022-12-06/decoder_jit_trace-pnnx.ncnn.param",
        decoder_bin="./sherpa-ncnn-conv-emformer-transducer-2022-12-06/decoder_jit_trace-pnnx.ncnn.bin",
        joiner_param="./sherpa-ncnn-conv-emformer-transducer-2022-12-06/joiner_jit_trace-pnnx.ncnn.param",
        joiner_bin="./sherpa-ncnn-conv-emformer-transducer-2022-12-06/joiner_jit_trace-pnnx.ncnn.bin",
        num_threads=4
    )

    fliename = "./sherpa-ncnn-conv-emformer-transducer-2022-12-06/test_wavs/0.wav"
    with wave.open(fliename) as f:
        assert f.getframerate() == recognizer.sample_rate,(
            f.getframerate(),
            recognizer.sample_rate
        )
        assert f.getnchannels() == 1, f.getnchannels()
        assert f.getsampwidth() == 2, f.getsampwidth()
        num_samples = f.getnframes()
        samples = f.readframes(num_samples)
        samples_int16 = np.frombuffer(samples, dtype=np.int16)
        samples_float32 = samples_int16.astype(np.float32)

        samples_float32 = samples_float32 / 32768

    recognizer.accept_waveform(recognizer.sample_rate, samples_float32)

    tail_paddings = np.zeros(int(recognizer.sample_rate * 0.5), dtype=np.float32)
    recognizer.accept_waveform(recognizer.sample_rate, tail_paddings)

    recognizer.input_finished()

    print(recognizer.text)

if __name__ == "__main__":
    main()




