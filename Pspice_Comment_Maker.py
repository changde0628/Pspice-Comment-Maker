#Author : changde0628

import sys
input_FileName = list(sys.argv)[1]
output_File = open("output.txt",'a')
input_file = open(input_FileName,encoding="UTF-8")
data_input = input_file.readlines()
data_input_size = len(data_input)
output_File.truncate(0)
sin_statment = ["直流位準","振幅","頻率","延遲","衰減","相位"]
pulse_statment = ["起始電壓","脈衝電壓","延遲時間","上升時間","下降時間","脈衝寬度","週期"]
for lines in data_input:
    process_lines = list(lines.strip().split())
    if(lines=="\n"):
        continue
    if(process_lines[0]==".probe"):
        tmp_write = "顯示波型 "
    elif(process_lines[0]==".op"):
        tmp_write = "顯示所有節點數據 "
    elif(process_lines[0]==".end"):
        tmp_write = "end of file"
    elif(process_lines[0]==".AC"):
        tmp_write = "交流電路分析 掃描點數"+process_lines[2]+"從"+process_lines[3]+"Hz到"+process_lines[4]+"Hz"
    elif(process_lines[0]==".TRAN"):
        tmp_write = "時間掃描分析 "+process_lines[1]+"~"+process_lines[2]
    elif(process_lines[0]==".model"):
        tmp_write = "模型"+process_lines[1]+" "+process_lines[2].replace("kp","製程互導參數")+" "+process_lines[3].replace("Vto","零偏壓臨界電壓")
        if(lines.find("lambda")!=-1):
            tmp_write += " "
            tmp_write += process_lines[4].replace("lambda","通道調變效應")
        output_File.write(lines.strip()+"\n"+"*"+tmp_write+"*"+"\n")
        continue
    elif(lines[0][0]=="V"):
        if(process_lines[3][0]=="S"):
            tmp_write = "宣告交流電壓源"+process_lines[0]+" 正端接"+process_lines[1]+" 負端接"+process_lines[2]
            tmp_sin_counter = len(process_lines)-3
            for i in range(tmp_sin_counter):
                sin_data_split = (process_lines[3+i].replace("SIN(","").replace(")",""))
                tmp_write += (" "+sin_statment[i]+"="+sin_data_split)
            output_File.write(lines.strip()+"\n"+"*"+tmp_write+"*"+"\n")
            continue
        elif(process_lines[3][0]=="D"):
            tmp_write = "宣告直流電壓源"+process_lines[0]+" 正端接"+process_lines[1]+" 負端接"+process_lines[2]+" 電壓值"+process_lines[4]
        elif(process_lines[3][0]=="p"):
            tmp_write = "宣告方波"+process_lines[0]+"正端接"+process_lines[1]+" 負端接"+process_lines[2]
            tmp_pulse_counter = len(process_lines)-3
            for i in range(tmp_pulse_counter):
                pulse_data_split = (process_lines[3+i].replace("pulse(","").replace(")",""))
                tmp_write += (" "+pulse_statment[i]+"="+pulse_data_split)
            output_File.write(lines.strip()+"\n"+"*"+tmp_write+"*"+"\n")
            continue
        else:
            tmp_write = "宣告直流電壓源"+process_lines[0]+" 正端接"+process_lines[1]+" 負端接"+process_lines[2]+" 電壓值"+process_lines[3]
    elif(lines[0][0]=="C"):
        tmp_write = "宣告電容"+process_lines[0]+" 正端接"+process_lines[1]+" 負端接"+process_lines[2]+" 電容值"+process_lines[3]+"F"
    elif(lines[0][0]=="R"):
        tmp_write = "宣告電阻"+process_lines[0]+" 正端接"+process_lines[1]+" 負端接"+process_lines[2]+" 電阻值"+process_lines[3]+"Ω"
    elif(lines[0][0]=="I"):
        if(process_lines[3][0]=="D"):
            tmp_write = "宣告電流源"+process_lines[0]+" 正端接"+process_lines[1]+" 負端接"+process_lines[2]+" 電流值"+process_lines[4]
        else:
            tmp_write = "宣告電壓源"+process_lines[0]+" 正端接"+process_lines[1]+" 負端接"+process_lines[2]+" 電流值"+process_lines[3]
    elif(lines[0][0]=="M"):
        tmp_write = "宣告"+process_lines[5]+" "+process_lines[0]+" D G S B 電晶體模型 匣極長度 匣極寬度"
        output_File.write(lines.strip()+"\n"+"*"+tmp_write+"*"+"\n")
        continue
    else:
        output_File.write(lines)
        continue
    output_File.write(lines.strip()+" *"+tmp_write+"*"+"\n")
print("已成功生成檔案output.txt")
input_file.close()
output_File.close()



