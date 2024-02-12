import pandas as pd

list1:list[str] = ["spammer", "suspicious", "category", "count_distinct_daily", "count_total_daily"]
# list2:list[int] = ["date", "spammer", "country_code", "country"] + list1[1:]

print(f"list2: {list1[0:5]}")


# for i in range(0, 10, 2):
#     print(' ', i)

# print(round())

def test_tuples():
    prefix_list = ['336-337', '001-023', '232', '0-3', '56-62']
    range_pre_list, single_pre_list = [], []

    for pre in prefix_list:
        index = pre.find('-')
        if index != -1:
            range_pre_list.append((index, pre))
        else:
            single_pre_list.append(pre)

    # range_pre_list = [(pre, 0) for pre in prefix_list ]

    print(range_pre_list)


def test_unpack_dict_values():
    dict_1 = {"key1": 111, "key2": [1, 2, 3, 4, 4], "key3": {"key1": 1}}
    dict_2 = {key: value for key, value in dict_1.items()}

    print(dict_2)

def test_dataframe_to_dict():
    # reading csv file from url
    data = pd.read_csv("/home/ziad/work/fraud-platform/kedro/detsi-spam/etc/prefix_list.tsv", header=None)

    # dropping null value columns to avoid errors
    data.dropna(inplace=True)

    # converting to dict
    data[0] = data[0].astype(str)
    data_dict = data[0].values.tolist()
    prefix_dict = {}
    for i in data_dict:
        prefix_dict[i] = i
    print(prefix_dict)

def test_split_string_fun():
    string ="""--__QUERY__
ALTER TABLE
{{db_name}}.{{pre_agg_sliding_table}} DELETE
WHERE
start_day < {{period_start}}
and start_day = {{today}};
--__END_QUERY__


-- Get sliding window for the last 2 days (today and yesterday) to consider the time 00:00 -1 hour
--__QUERY__
INSERT INTO TABLE {{db_name}}.{{pre_agg_sliding_table}} 
SELECT
toYYYYMMDD(a.start_time) AS start_day,
a.a_number as a_number,
max(a.moving_uniq_count_1_hour) as max_sliding_count
FROM
"""

    queries_raw = string.split("\n--__QUERY__\n")[1:]


    print('---------------------------------')
    print(string)
    for q in queries_raw:
        print(q)
        print('---------------------------------')


def test_split_string_fun2():
    str = f"""--
1
--
2
--
3"""

    print(str.split("\n--__QUERY__\n")[1:])
    # print(f"\nAAA\nBB")