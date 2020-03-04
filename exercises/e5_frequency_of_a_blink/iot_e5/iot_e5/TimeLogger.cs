using System;
using System.IO;
using System.IO.Ports;
using System.Threading;

namespace iot_e5
{
    public class TimeLogger
    {

        private SerialPort _serialPort;
        
        
        private string _filePath = System.IO.Directory.GetCurrentDirectory() + "/out.txt";
        
        
        public TimeLogger()
        {
            _serialPort = new SerialPort("/dev/ttyACM0", 115200, Parity.None, 8, StopBits.One);
            
            _serialPort.Open();
            
            ReadInput();
        }

        private void ReadInput()
        {
            using (StreamWriter sw = File.CreateText(_filePath))
            {
                while (true)
                {
                    var readByte = _serialPort.ReadByte();
                    Console.WriteLine(readByte);
                    sw.WriteLine(DateTime.Now.Millisecond);
                }
            }
        } 
    }
}