# Audio-Mango

Lightweight program for encoding data into audio, written in Python.

**Some dependencies**  

* [Pillow](http://python-pillow.org/) - A fork of PIL (Python Imaging Library)  
* [PyDub](http://pydub.com/) - Audio manipulator  

[Sonic Visualiser](https://www.sonicvisualiser.org/) is a really awesome audio analyser application. I recommend using it for viewing the generated spectrograms.  

![SomethingAwesome](include/repo/mango.jpg?raw=true)

 -----------------------------------------------------------

### Usage 

Storage for all input/audio files that you want to process should be placed accordingly into these directories. Please do so, the program's path lookup revolves around them!   
* Audio collection (not for processing, just for convenience) ```include/lib/``` 
* Sliced audio (to-be processed), needn't worry about this as slicer.py should handle this ```include/slice_lib/```
* Input files that you want to hide ```include/payload_lib/```  

------------------------------------------------------------

**slicer.py**. I have also written a simple slicer script that, you guessed it, slices audio.  

```
usage: slicer.py [-h] [-fi FADEIN] [-fo FADEOUT] input lo hi

positional arguments:
  input                 input file that exists in lib. Not path.
  lo                    lowerbound (sec)
  hi                    upperbound (sec)

optional arguments:
  -h, --help            show this help message and exit
  -fi FADEIN, --fadein FADEIN
                        fade in offset (sec)
  -fo FADEOUT, --fadeout FADEOUT
                        fade out offset (sec)
```  

----------------------------------------------

**make.py** is the entry point for production. Grabs the files according to the input filenames and stores the modified audio in ```lsb/``` or ```spec/``` accordingly.  


```
usage: make.py [-h] [-m MODE] input medium output

positional arguments:
  input                 Payload file in payload_lib. Don't input path.
  medium                The audio file in slice_lib. Don't input path.
  output                Set the output filename

optional arguments:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  Select mode: lsb or spec

```  

-----------------------------------------------------   

**extract.py** is the entry point for extraction *(duh)*. Grabs the requested file from ```lsb/``` *(spec extraction not implemented yet)* and stores the retrieved payload into ```extracted_payloads/```.  


```
usage: extract.py [-h] input num_bytes

positional arguments:
  input       The wav file holding the data. Don't input path to file.
  num_bytes   The number of bytes to recover

optional arguments:
  -h, --help  show this help message and exit
```  

---------------------------------------------------------

**References**  
Super helpful audio processing resources and some interesting articles.

* [Visual Cryptography](http://www.datagenetics.com/blog/november32013/index.html) - Decrpytion with the human eye
* [Image-Encode](http://www.ohmpie.com/imageencode/) - Image Encoding
* [Image transforms](https://plus.maths.org/content/fourier-transforms-images) - Fourier transforms of images
