

def average_len(records):
    """This function allows to get an average length of lists in set"""
    return round(sum(len(record) for record in records) / len(records))

def average_len_taxa(records):
    """This function allows to calculate average length for different groups"""
    record_by_taxa = {}
    for r in records:
        taxa = r.annotations["taxonomy"][0]
        record_by_taxa.setdefault(taxa, []).append(r)

    return {taxa:average_len(record) for (taxa, record) in record_by_taxa.items()}
