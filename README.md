<div align="center">
  <a href="https://github.com/aorumbayev/autogpt4all">
    <img src="https://bafkreif7cbmuvhztfdlscnmgi3ob32d6ulkqgbjqy4cff2krth4dynwwhe.ipfs.nftstorage.link">
  </a>
</div>

<p align="center">
    <img  src="https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Faorumbayev%2Fautogpt4all&countColor=black&style=flat" />
    <a target="_blank" href="https://github.com/aorumbayev/autogpt4all"><img src="https://img.shields.io/github/stars/aorumbayev/autogpt4all?color=black" /></a>
    <a target="_blank" href="https://github.com/aorumbayev/2Fautogpt4all/network/members"><img src="https://img.shields.io/github/forks/aorumbayev/autogpt4all?color=black" /></a>
</p>

AutoGPT4All provides you with both bash and python scripts to set up and configure [AutoGPT](https://github.com/Significant-Gravitas/Auto-GPT.git) running with the [GPT4All](#) model on the [LocalAI](https://github.com/go-skynet/LocalAI) server. This setup allows you to run queries against an open-source licensed model without any limits, completely free and offline.

> If you are interested in building decentralized applications, check out my other repo at [AwesomeAlgorand](https://github.com/aorumbayev/awesome-algorand).

## 🚀 Quickstart

### Using Bash Script:

```sh
git clone https://github.com/aorumbayev/autogpt4all.git
cd autogpt4all
chmod +x autogpt4all.sh
./autogpt4all.sh
```

### Using Python Script:

Make sure you have Python installed on your machine.

```sh
git clone https://github.com/aorumbayev/autogpt4all.git
cd autogpt4all
python autogpt4all.py
```

> ❗️ Please note this script has been primarily tested on MacOS with an M1 processor. It should work on Linux and Windows, but it has not been thoroughly tested on these platforms. If not on MacOS install git, go and make before running the script.

## 🎛️ Script Options

### For the bash script:

`--custom_model_url` - Specify a custom URL for the model download step. By default, the script will use https://gpt4all.io/models/ggml-gpt4all-l13b-snoozy.bin.

Example:

```
./autogpt4all.sh --custom_model_url "https://example.com/path/to/model.bin"
```

`--uninstall` - Uninstall the projects from your local machine by deleting the LocalAI and Auto-GPT directories.

Example:

```
./autogpt4all.sh --uninstall
```

> To recap the commands, a --help flag is also available for the bash script.

### For the Python Script:

You can use similar options as the bash script:

`--custom_model_url` - Specify a custom URL for the model download step.

Example:

```sh
python autogpt4all.py --custom_model_url "https://example.com/path/to/model.bin"
```

`--uninstall` - Uninstall the projects from your local machine.

Example:

```sh
python autogpt4all.py --uninstall
```

## 💡 Notes

-   The script checks if the directories exist before cloning the repositories.
-   On macOS, the script installs cmake through brew. Please make sure you have brew installed. On Linux its assumed you have apt-get installed.
-   A custom model URL can be passed if the default model link changes or is unavailable.

## 🤝 Contributing

Please feel free to contribute to this project. Any kind of contribution would be greatly appreciated. To contribute, please:

1. Fork the repo.
2. Make your changes.
3. Submit a pull request.

## 📜 License

MIT License. See LICENSE for more information.

## ⭐️ Stargazers

Special thanks to everyone who starred the repository ❤️

[![Stargazers repo roster for @aorumbayev/autogpt4all](https://reporoster.com/stars/dark/aorumbayev/autogpt4all)](https://github.com/aorumbayev/autogpt4all/stargazers)
