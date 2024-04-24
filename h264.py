class NALU:
    def __init__(self, prefix, header, type, payload):
        self.prefix = prefix
        self.header = header
        self.type = type
        self.payload = payload

def parse_h264_nalu(bitstream):
    forbidden_zero_bit = (bitstream[0] & 0b10000000) >> 7
    nal_ref_idc = (bitstream[0] & 0b01100000) >> 5
    nal_unit_type = (bitstream[0] & 0b00111111)

    # Calculate header length based on the specific NALU type
    header_length = 1  # Assuming 1-byte header for simplicity
    if nal_unit_type in [1, 2, 3, 4, 5]:
        # These NALU types have extended headers
        header_length += 2  # Adjust the length as needed

    # Extract payload based on header length
    payload = bitstream[header_length:]

    return nal_unit_type, bitstream[:header_length], payload

def parse_h264(h264_file_path):
    with open(h264_file_path, 'rb') as file:
        bytestream = file.read()
    
    video = []
    
    start_code_prefix =  b"\x00\x00\x01"

    nalu_end = 0
    while bytestream:
        nalu_start = bytestream.find(start_code_prefix)

        if nalu_start != 0:
            video.append(bytestream[:nalu_start])

        # Locate the end of the NALU (start of the next NALU or end of the bitstream)
        nalu_end = bytestream.find(start_code_prefix, nalu_start + len(start_code_prefix))

        prefix = bytestream[nalu_end:nalu_start]+start_code_prefix
        if nalu_end == -1:
            nalu_end = len(bytestream)

        if nalu_end-nalu_start > len(start_code_prefix):
            nal_unit_type, header, payload = parse_h264_nalu(bytestream[nalu_start+len(start_code_prefix):nalu_end])
            video.append(NALU(prefix,header,nal_unit_type,payload))
        else:
            video.append(bytestream[nalu_start:nalu_end])
        bytestream = bytestream[nalu_end:]
    return video
    