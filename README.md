# sample_slicer_caustic3
A script for slicing samples and package them for easy import in Caustic 3
Slices up an audio file into a set amount of slices of equal length. Best performance is achieved if sample is quantized before slicing.

# Usage: 
python3 ./slice_sample.py path/to/sample.wav number_of_slices (optional: preview before zipping, can be anything)

Example: python3 ./slice_sample.py amen_break.wav 32 preview <- Will chop your Winstons break into 32 slices without zipping them,
producing samples with the following naming convention: 000slice_C0.wav ... 031slice_G2.wav
Example: python3 ./slice_sample.py amen_break.wav 32 banana <- same as above example

Example: python3 ./slice_sample.py amen_break.wav 8 <- Will chop your Winstons break into 8 slices, adding them to a zip file called 8_amen_break.zip,
containing samples with the following naming convention: 000slice_C0.wav ... 007slice_G0.wav

Example:  python3 ./slice_sample.py Rhythm\ Lab\ Neu\ Jungle\ Preview/Breaks/168\ Kungfu\ Break\ 2.wav 64 
Will chop your Kungfu break into 64 slices, adding them to a zip file called 64_168_Kungfu_Break_2.zip,
containing samples with the following naming convention: 000slice_C0.wav ... 007slice_G0.wav


# Requirements: 
requires pydub: pip3 install pydub
