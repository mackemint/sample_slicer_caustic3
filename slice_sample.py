from zipfile import ZipFile
from pydub import AudioSegment
import sys, os, glob

sound = AudioSegment.from_wav(sys.argv[1])
slice_length = int(len(sound) / int(sys.argv[2]))
slice_indicator = "slice_"
audio_range = int(len(sound)/(len(sound) / int(sys.argv[2])))
print(f"clip length: {len(sound)}")
print(f"slice length: {slice_length}")
print(f"slicing {sys.argv[1]} to {sys.argv[2]} slices ...")


note = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
note_count = 0
octave = 1
offset = 0
incrementor = 0
for sl in range(audio_range):
	number_slice = '{:03}'.format(incrementor)
	slice_name = f"{number_slice}{slice_indicator}{note[note_count]}{octave}.wav"
	print(f"slicing {slice_name}")
	slice_part = sound[offset:offset+slice_length]
	slice_part.export(slice_name, format="wav")
	note_count += 1
	incrementor += 1
	offset += slice_length
	if note_count == 12:
		note_count=0
		octave+=1
	if incrementor == 128:
		break

file_name = glob.glob(f'./*{slice_indicator}*.wav')
if len(sys.argv) < 4:
	with ZipFile(f'{sys.argv[2]}_chopped.zip', 'w') as myzip:
		for f in file_name:
			myzip.write(f)
			os.remove(f)
	print("Archive created.")
else:
	print("Slicing complete, please preview your files")
