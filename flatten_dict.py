def flatten_dict(original_dict):
    '''
    creates a new dictionnary with each value that is not a dictionnary is assigned to an aggregate key made from 
    all fond at all levels of depth
    '''
    flat_dict = {}
    for k,v in original_dict.items():
        if type(v) is dict:
            if v:
                new_key = k + '/'
                for k,v in flatten_dict(v).items():
                    flat_dict[new_key + k] = v
            else:
                flat_dict[k] = ""
        else:
            flat_dict[k] = v
    return flat_dict
            

if __name__ == '__main__':
    assert flatten_dict({"key": "value"}) == {"key": "value"}
    assert flatten_dict({"key": {"deeper": {"more": {"enough": "value"}}}}) == {"key/deeper/more/enough": "value"}
    assert flatten_dict({"empty": {}}) == {"empty": ""}

