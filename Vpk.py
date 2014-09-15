print 'Welcomme to the Undecidedname,'
print 'DotA 2 must be installed on this pc in order for this program to work.'

import os,struct,binascii,logging

logger = logging.getLogger(__name__)

class vpkFile(object):
	def __init__(self, vpk):
		self._vpk_files = vpk
		self._vpklist = []
	def read(self):
		logger.info('Beginning to extract the VPK files')
		for vf in self.vpk_files:
			print(vf.path,"({} bytes)".format(len(vf.preload)+vf.length))
			full_path = os.path.join(os.getcwd(),"vpk_extracted",vf.path.replace("/","\\"))
			dir = os.path.dirname(full_path)
			if not os.path.isdir(dir):
				os.makedirs(dir)
			out_data = open(full_path,'wb')
			out_data.write(vf.preload)
			if vf.length:
				vpk = open("pak01_{}.vpk".format(str(vf.archive_index).zfill(3)),'rb')
				vpk.seek(vf.offset)
				out_data.write(vpk.read(vf.length))
				vpk.close()
			out_data.close()

class structunpack():
	def _get_int4(self):
		return int( struct.unpack("I",index.read(4))[0] )
	def _get_int2(self):
		return int( struct.unpack("H",index.read(2))[0] )
	
	def _get_sz(self):
		out = ""
		while True:
			cur = index.read(1)
			if cur == b'\x00': break
			out += struct.unpack("c",cur)[0].decode("ASCII")
		return out
	
	def open(self, fileName):
		index = open(fileName, 'rb')
		logger.info( "Signature:",binascii.b2a_hex(index.read(4)) )
		logger.info( "Version:",get_int4() )
		logger.info( "Directory length:", get_int4() )
		logger.info( "Unknown1:", get_int4() )
		unknown2 = get_int4() # footer length?
		logger.info( "Unknown2:", unknown2 )
		unknown3 = get_int4()
		logger.info( "Unknown3:", unknown3 )
		logger.info( "Unknown4:", get_int4() )
		
		path = ""
		CRC = -1
		archive_index = -1
		offset = -1
		length = -1
		preload = bytes()
		vpk_files = []
    
		while True:
			extension = get_sz()
			if not extension: break		
			
			while True:
				folder = get_sz()
				if not folder: break
				
				while True:
					filename = get_sz()
					if not filename: break
					
					cur_file = VpkFile()
					vpk_files.append(cur_file)
					cur_file.path = "{}/{}.{}".format(folder,filename,extension)
					
					cur_file.CRC = get_int4()
					preload_bytes = get_int2()
					cur_file.archive_index = get_int2()
					if cur_file.archive_index == b'\x7fff':
						logger.info("EMBED")
					cur_file.offset = get_int4()
					cur_file.length = get_int4()
					get_int2() # terminator
					
					if preload_bytes:
						cur_file.preload = index.read(preload_bytes)
	 
	    	index.close()
	    return vpkFile(vpk_files)
	
