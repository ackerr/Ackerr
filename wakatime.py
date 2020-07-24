import re
import requests

gist = "https://gist.githubusercontent.com/Ackerr/22090c7f0e7817c8369b65d66c91982e/raw/"


if __name__ == "__main__":
    response = requests.get(gist)
    wakatime = f"\n```text\n{response.text}\n```\n"

    template = "<!-- WakaTime Start -->{}<!-- WakaTime End -->"

    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()

    with open("README.md", "w", newline="\n", encoding="utf-8") as f:
        r = re.compile(template.format(".*"), re.DOTALL)
        content = r.sub(template.format(wakatime), readme)
        f.write(content)
