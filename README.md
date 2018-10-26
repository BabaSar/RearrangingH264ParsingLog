# RearrangingH264ParsingLog
Rearranging A/V Codec analyser's H264 Parsing log from Decode order to Presentation Order

When using A/V Codec analyser, the output h264 parsing log is given in decode order. 
However, you may want this to instead be presented in presentation order to correctly calculate GOP length for example. 
It has been seen that A/V incorrectly calculates GOP lengths based on decode order, which is not what we want.
