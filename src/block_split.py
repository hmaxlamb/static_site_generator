def markdown_to_blocks(markdown):
    block_o_block_list = []
    block_list = []
    lines = markdown.split("\n")
    for line in lines:
        if line == "":
            block_o_block_list.append(block_list)
            block_list = []
        else:
            new_line = line.strip()
            block_list.append(new_line)
    if block_list != []:
        block_o_block_list.append(block_list)
    
    return_list = []

    for block in block_o_block_list:
        new_block = "\n".join(block)
        if new_block == "":
            continue
        return_list.append(new_block)

    return return_list


def block_to_block_type(block):
    if block[:1] == "#":
        heading = "# "
        for i in range(2, 8):
            if block[:(i)] == heading:
                return f"heading{(i - 1)}"
            else:
                heading = "#" + heading
    
    if block[:3] == "```" and block[-3:] == "```":
        return "code"
    
    if block [:1] == ">":
        split_blocks = block.split("\n")
        for line in split_blocks:
            if line[:1] == ">":
                continue
            else:
                return "paragraph"
        return "quote"
    
    if block [:2] == "* ":
        split_blocks = block.split("\n")
        for line in split_blocks:
            if line[:2] == "* ":
                continue
            else:
                return "paragraph"
        return "unordered_list"
    
    if block [:2] == "- ":
        split_blocks = block.split("\n")
        for line in split_blocks:
            if line[:2] == "- ":
                continue
            else:
                return "paragraph"
        return "unordered_list"
    
    if block [:2] == "1.":
        split_blocks = block.split("\n")
        line_count = len(split_blocks)
        for i in range(1, (line_count + 1)):
            if split_blocks[(i - 1)][:2] == f"{i}.":
                continue
            else:
                return "paragraph"
        return "ordered_list"
    
    return "paragraph"
