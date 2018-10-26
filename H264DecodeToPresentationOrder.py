filename = "H264_Parsing.log"
import re
 
lines = []
gop_decode_order = []
gop_presentation_order = []
 
with open(filename) as fileobject:
    for line in fileobject:
        if "FrameType" in line:
            lines.append(line.rstrip())
 
presentation_index = [] #need to sort this by number
presentation_index_number_only = []
 
pattern = re.compile(r'PresentationIndex\[(.*?)\]') #r tells Python not to interpret the backslashes
 
for i in range(len(lines)):
    presentation_index.append(pattern.search(lines[i]).group()) #group() extracts the match from the obj
 
for i in range(len(presentation_index)):
    number = presentation_index[i].strip("PresentationIndex[").strip("]")
    presentation_index_number_only.append(number)
 
presentation_index_number_only = [int(x) for x in presentation_index_number_only]
presentation_index_number_only.sort()
 
presentation_index_number_only = [str(x) for x in presentation_index_number_only]
 
presentation_index_sorted = []
 
for presentation_index in presentation_index_number_only:
    if int(presentation_index) >= 0 and int(presentation_index) <= 9:
        presentation_index = f"PresentationIndex[ {presentation_index}]"
    else:
        presentation_index = f"PresentationIndex[{presentation_index}]"
    presentation_index_sorted.append(presentation_index)
 
output_variable = ""
 
for i in range(len(presentation_index_sorted)):
    # print(presentation_index_sorted[i])
    for line in lines:
        if presentation_index_sorted[i] in line:
            output_variable += line + "\n"
            print(line)
 
f = open("presentation_output.log", "w+")
f.write(output_variable)
 
print("Writing to file completed!")
