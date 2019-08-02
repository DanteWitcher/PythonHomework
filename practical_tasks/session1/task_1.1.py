def replace(string: str) -> str:
    string.replace('\'', '\"').replace('\"', '\'')
    return string


replace('"')

print('there should be \' equal {}, and \" equal {} '.format(replace('\', \'\', \'\'\''), replace('\", \"\", \"\"\"')))
