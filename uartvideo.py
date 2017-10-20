#!/usr/bin/python

class VideoPlayer:
	uartdev = None
	vlcprocess = None
	playing = False

	@staticmethod
	def initialize():
		import sys, tty, termios
		from subprocess import call
		call(["./init_dev.sh"])
		VideoPlayer.uartdev = open("/dev/ttyS2")
		old_settings = termios.tcgetattr(VideoPlayer.uartdev)
		tty.setraw(VideoPlayer.uartdev)
		call(["stty", "-F" "/dev/ttyS2", "115200"])

	@staticmethod
	def begin():
		print "Waiting for commands from UART 2, 115200 bps."
		while True:
			ch = VideoPlayer.uartdev.read(1)
			if ch == "P":
				filename = VideoPlayer.readString()
				VideoPlayer.play(filename)
			elif ch == "S":
				VideoPlayer.stop()

	@staticmethod
	def readString():
		str = ""
		while True:
			ch = VideoPlayer.uartdev.read(1)
			if ch == "\x00":
				break
			str += ch

		return str

	@staticmethod
	def play(filename):
		from subprocess import Popen
		import os, os.path
		if not os.path.isfile(filename):
			print "File '" + filename + "' not found."
			return
		print "Playing file '" + filename + "'."
		DEVNULL = open(os.devnull, "w")
		VideoPlayer.stop()
		VideoPlayer.vlcprocess = Popen(["vlc", "--fullscreen", filename], stdout = DEVNULL, stderr = DEVNULL)

		VideoPlayer.playing = True
		return

	@staticmethod
	def stop():
		if VideoPlayer.playing:
			print "Stopped."
			VideoPlayer.vlcprocess.terminate()
			VideoPlayer.vlcprocess.wait()

			VideoPlayer.playing = False

VideoPlayer.initialize()
VideoPlayer.begin()

# termios.tcsetattr(uartdev, termios.TCSADRAIN, old_settings)
