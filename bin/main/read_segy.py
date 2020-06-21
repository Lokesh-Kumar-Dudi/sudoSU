import os

class segy():
    def convert(self,arg):
        i=0
        while (arg>1024):
            arg=arg/1024
            i+=1
        size = str(int(arg))
        if i==2:
            return size+" MB"
        elif i==3:
            return size+" GB"
        elif i==4:
            return size+" TB"
        else:
            return size+" KB"

    def get_size(self,filename):
        if filename==None:
            pass
        else:
            return self.convert(os.stat(filename)[6])
    
    def get_trace_hdrs(self,filename,trace_no):
        segy = open(filename, 'rb')
        segy.seek(3220)
        n_samples = int.from_bytes(segy.read(2),byteorder='big')
        trace_info = open('trace_hdrs_info.txt','r')
        trace_hdrs={}
        size_trace=os.stat(filename)[6]-3200-400
        n_traces=int(size_trace/(n_samples*4+240))
        if trace_no>n_traces:
            trace_hdrs['Invalid Trace No.']=str(trace_no)
        else:
            for line in trace_info:
                line.rstrip()
                line = line.split()
                string=""
                for i in line[2:]:
                    string+=" "+i
                segy.seek(3600+(n_samples*4+240)*(trace_no-1)+int(line[0])-1)
                trace_hdrs[string]=str(int.from_bytes(segy.read(int(line[1])),byteorder='big')) 
        trace_info.close()
        segy.close()
        return trace_hdrs

    def get_binary_hdrs(self,filename):
        file_size = os.stat(filename)[6]
        segy = open(filename, 'rb')
        binary_data={}
        segy.seek(3200)
        binary_data["Job identification number : "]=str(int.from_bytes(segy.read(4),byteorder='big'))
        segy.seek(3204)
        binary_data["Line number : "]=str(int.from_bytes(segy.read(4),byteorder='big'))
        segy.seek(3208)
        binary_data["Reel No: "]=str(int.from_bytes(segy.read(4),byteorder='big'))
        segy.seek(3212)
        binary_data["Number of data traces per ensemble : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.seek(3214)
        binary_data["Number of auxiliary traces per ensemble : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.seek(3216)
        binary_data["Sample interval : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.seek(3218)
        binary_data["Sample interval of original field recording : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.seek(3220)
        binary_data["Number of samples per data trace : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.seek(3222)
        binary_data["Number of samples per data trace for original field recording : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.seek(3220,0)                                  # Locate our position to 3221th byte of file                              # Read 2 byte from our position
        binary_data["Number of traces in this file : "]=str(int((file_size-3200-400)/(int.from_bytes(segy.read(2), byteorder='big')*4+240)))
        segy.seek(3224)
        binary_data["Data sample format code : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.seek(3226)
        binary_data["Ensemble fold : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.seek(3228)
        binary_data["Trace sorting code : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.seek(3230)
        binary_data["Vertical sum code : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.seek(3232)
        binary_data["Sweep frequency at start(Hz) : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.seek(3234)
        binary_data["Sweep frequency at send(Hz) : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.seek(3236)
        binary_data["Sweep length(ms) : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.seek(3238)
        binary_data["Sweep type code : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.seek(3240)
        binary_data["Trace number of sweep channel : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.seek(3242)
        binary_data["Sweep trace taper length at start(ms) : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.seek(3244)
        binary_data["Sweep trace taper length at end(ms) : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.seek(3246)
        binary_data["Taper type : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.seek(3248)
        binary_data["Correlated data traces : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.seek(3250)
        binary_data["Binary gain recovered : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.seek(3252)
        binary_data["Amplitude recovery method : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.seek(3254)
        binary_data["Measurement system : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.seek(3256)
        binary_data["Impulse signal polarity : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.seek(3258)
        binary_data["Vibratory polarity code : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.seek(3260)
        binary_data["Extended number of data traces per ensemble : "]=str(int.from_bytes(segy.read(4),byteorder='big'))
        segy.seek(3264)
        binary_data["Extended number of auxiliary traces per ensemble : "]=str(int.from_bytes(segy.read(4),byteorder='big'))
        segy.seek(3268)
        binary_data["Extended number of samples per data trace : "]=str(int.from_bytes(segy.read(4),byteorder='big'))
        segy.seek(3272)
        binary_data["Extended sample interval : "]=str(int.from_bytes(segy.read(8),byteorder='big'))
        segy.seek(3280)
        binary_data["Extended sample interval of original field recording : "]=str(int.from_bytes(segy.read(8),byteorder='big'))
        segy.seek(3288)
        binary_data["Extended number of samples per data trace in original recording : "]=str(int.from_bytes(segy.read(4),byteorder='big'))
        segy.seek(3292)
        binary_data["Extended ensemble fold : "]=str(int.from_bytes(segy.read(4),byteorder='big'))
        segy.seek(3500)
        binary_data["Major SEG-Y Format Revision Number : "]=str(int.from_bytes(segy.read(1),byteorder='big'))
        segy.seek(3501)
        binary_data["Minor SEG-Y Format Revision Number : "]=str(int.from_bytes(segy.read(1),byteorder='big'))
        segy.seek(3502)
        binary_data["Fixed length trace flag : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.seek(3504)
        binary_data["Number of 3200-byte Extended Textual File Header records  : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.seek(3506)
        binary_data["Maximum number of additional 240 byte trace headers  : "]=str(int.from_bytes(segy.read(4),byteorder='big'))
        segy.seek(3510)
        binary_data["Time basis code  : "]=str(int.from_bytes(segy.read(2),byteorder='big'))
        segy.close()
        return binary_data

    def get_ebcdic_hdrs(self,filename):
        file_size = os.stat(filename)[6]
        segy = open(filename, 'rb')
        ebcdic_data=[]
        segy.seek(0,0)
        data = segy.read(3200)         
        data = data.decode('cp500') 
        n = 80                      
        txt_header=[]               
        for i in range(0, len(data), n):  
            txt_header.append(data[i:i+n])  
        for i in range(0,len(txt_header)):
            ebcdic_data.append(txt_header[i])
        segy.close()
        return ebcdic_data

