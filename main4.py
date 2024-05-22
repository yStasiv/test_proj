# Вхідні дані
f = [
    "RULE_1        DATAACL         9999              101            100",
    "RULE_2        DATAACL         9998              201            200",
    "RULE_3        DATAACL         9997              301            300",
    "RULE_4        DATAACL         9996              401            400",
    "RULE_05       DATAACL         9995                0              0",
    "RULE_7        DATAACL         9993              701            700",
    "RULE_9        DATAACL         9991              901            900",
    "DEFAULT_RULE  DATAACL            1                2              1",
    "RULE_6        EVERFLOW        9994              601            600",
    "RULE_08       EVERFLOW        9992                0              0"
]

def parse_line(line):
    data_item = line.split()
    rule_name = data_item[0]
    table_name = data_item[1]
    prio = int(data_item[2])
    packets_count = int(data_item[3])
    bytes_count = int(data_item[4])
    return (rule_name, table_name, prio, packets_count, bytes_count)

parsed_data = [parse_line(line) for line in f]

sorted_data = sorted(parsed_data, key=lambda x: (x[1], x[2]))


if __name__ == "__main__":
    print(f"{'RULE NAME':<12}  {'TABLE NAME':<12}  {'PRIO':<6}  {'PACKETS COUNT':<15}  {'BYTES COUNT':<13}")
    print(f"{'-' * 12}  {'-' * 12}  {'-' * 6}  {'-' * 15}  {'-' * 13}")
    for entry in sorted_data:
        print(f"{entry[0]:<12}  {entry[1]:<12}  {entry[2]:<6}  {entry[3]:<15}  {entry[4]:<13}")