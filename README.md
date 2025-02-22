# lm-sentiment-analyzer

This project is a standalone backend solution for sentiment analysis of textual data. The sentiment is determined using language models, with the flexibility to choose between different models.

**Currently Available Language Models:**
- [cardiffnlp/twitter-xlm-roberta-base-sentiment](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment)
- [tabularisai/multilingual-sentiment-analysis](https://huggingface.co/tabularisai/multilingual-sentiment-analysis)

*Note: This project was developed as part of a university seminar and has been migrated to this repository.*


<!-- Getting Started -->
## <img align="center" width="60px" height="60px" src="https://media3.giphy.com/media/wuZWV7keWqi2jJGzdB/giphy.gif?cid=6c09b952wp4ev7jtywg3j6tt7ec7vr3piiwql2vhrlsgydyz&ep=v1_internal_gif_by_id&rid=giphy.gif&ct=s"> Get Started <a id="started"></a>

<!-- Docker -->
### <img align="center" width="60px" src="https://miro.medium.com/v2/resize:fit:1400/1*wXtyhpOL5NK_w39UvZpADQ.gif"> Docker <a id="docker"></a>
1. **Install Docker**<br>
    For more information on installing Docker, please visit the official Docker website: [Install Docker Engine](https://docs.docker.com/engine/install/)
2. **Clone the Repository**
    ```bash
    $ git clone https://github.com/lukasschr/lm-sentiment-analyzer.git
    $ cd lm-sentiment-analyzer
    ```
3. **Build Image**
    ```bash
    $ make build
    # or:
    # docker build -t lm-sentiment-analyzer:prod .
    ```
4. **Start Docker Container (Port 8000)**
    ```bash
    $ make run
    # or:
    # docker run -d -p 8000:8000 --name lm-sentiment-analyze lm-sentiment-analyzer:prod
    ```
5. **Stop Docker Container**
    ```bash
    $ make stop
    # or:
    # docker stop lm-sentiment-analyze
    ```
6. **Delete Docker Container & Image**
    ```bash
    $ make delete
    # or:
    # docker rm lm-sentiment-analyze
    # docker rmi lm-sentiment-analyzer:prod
    ```

<!-- Contact -->
## Contact

**Lukas Schröder** | [LinkedIn](https://www.linkedin.com/in/lukasschr/)