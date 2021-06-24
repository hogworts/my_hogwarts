import yaml


class LoadData:
    def yaml_data(self):
        with open("../data/test_data.yml", "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        return data


if __name__ == '__main__':
    dt = LoadData()
    print(dt.yaml_data())
