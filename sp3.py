import os

class SP3:

	def __init__(self):
		self.video1min = "1min_bbb.mp4"
		self.videos = ["resized720_bbb.mp4","resized480_bbb.mp4","resized360_bbb.mp4","resized140_bbb.mp4"]
		self.ip = "224.2.2.2"
		self.capture_streaming = "ffplay -i udp://@" #+ 224.2.2.2:2222"
		self.port = ":2222"
	def convert_to_codec(self,codec):
		i=0
		if codec == "vp8":
			for video in self.videos:
				os.system("ffmpeg -i " + video + " -c:v libvpx -b:v 1M -c:a libvorbis vp8_"+str(i)+".webm")
				i+=1
		elif codec == "av1":
			for video in self.videos:
				os.system("ffmpeg -i " + video + " -c:v libaom-av1 -crf 30 -b:v 0 av1_"+str(i)+".mkv")
				i+=1
		elif codec == "vp9":
			for video in self.videos:
				os.system("ffmpeg -i " + video + " -c:v libvpx-vp9 -b:v 2M vp9_"+str(i)+".webm")
				i+=1
		elif codec == "h265":
			for video in self.videos:
				os.system("ffmpeg -i " + video + " -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k h265_"+str(i)+".mp4")
				i+=1
	def video_comparison(self,video1,video2):
		os.system("ffmpeg -i " + video1 + " -i " + video2 + " -filter_complex hstack comparison.webm")

	def broadcast_video(self, ip = "224.2.2.2"):
		os.system("ffmpeg -i " + self.video1min + " -f mpegts udp://@" + ip +":2222")
	
	def main(self):
		loop = True
		while loop:
			option = input("Input the exercise number you want to execute:\n1- Convert videos to the different codecs\n2- Showcase comparison between videos with diferent codecs(you will need to generate them first)\n3- Broadcast a video (you can choose the ip)\nAny other number to exit\n")
			if option.strip() == "1":
				codec = input("write the codec you want to convert the videos to: (vp8/vp9/av1/h265)")
				if codec.lower() == "vp8" or codec.lower() == "vp9" or codec.lower() == "av1" or codec.lower() == "h265":
					s.convert_to_codec(codec)
					#loop = False
				else:
					print("please enter a valid codec, returning to main menu")
			elif option.strip() == "2":
				video1 = input("enter the name of the 1 video (vp8_1.webm/vp9_1.webm/av1_1.mkv(very slow generation)/h265_1.mkv)\n").strip()
				video2 = input("enter codec of the 2 video (vp8_1.webm/vp9_1.webm/av1_1.mkv(very slow generation)/h265_1.mkv)\n").strip()
				s.video_comparison(video1,video2)
				print("the video is now on your folder as comparison.webm")
				print("Since we are converting all the diferent videos that might have different extensions in them into a packaged video, we are losing the possible diferences we could find in them. If we had two different files and we opened them at the same time, that is why we cant see very clear differences between any of the videos we generate here.")
				#loop = False
			elif option.strip() == "3":
				ip = input("please enter the UDP ip (just the last part (XXX.XXX , for example 2.23) you want to broadcast to, enter to use the default one: ")
				if ip != "":
					input("please enter this command on another command line in your computer:\n" + self.capture_streaming + "224.2." + ip + self.port)
					s.broadcast_video(ip = "224.2." + ip)
				else:
					input("please enter this command on another command line in your computer:\n" + self.capture_streaming + self.ip + self.port)
					s.broadcast_video()
			else:
				loop = False
if __name__ == "__main__":
	s = SP3()
	s.main()
	#s.convert_to_codec("vp9")
	#s.convert_to_codec("vp8")
	#s.convert_to_codec("h265")
	#s.video_comparison("vp8_1.webm","vp9_1.webm")
	#s.broadcast_video()
	#test= input()
	#print(test)
