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
        return_list.append(new_block)

    return return_list