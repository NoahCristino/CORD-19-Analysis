[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/NoahCristino/CORD-19-Analysis/">
    <img src="./logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">CORD-19 Analysis</h3>

  <p align="center">
    Analysis of the [CORD-19](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge/) dataset.
    <br />
    <!--<a href="https://github.com/NoahCristino/CORD-19-Analysis/"><strong>Explore the docs »</strong></a>-->
    <br />
    <br />
    <a href="https://github.com/NoahCristino/CORD-19-Analysis/issues">Report Bug</a>
    ·
    <a href="https://github.com/NoahCristino/CORD-19-Analysis/issues">Request Feature</a>
    ·
    <a href="https://github.com/NoahCristino/CORD-19-Analysis/pulls">Send a Pull Request</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)
* [Donations](#donations)



<!-- ABOUT THE PROJECT -->
## About The Project

This project is my contribution to helping to analyse the [CORD-19](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge/) dataset. This dataset contains thousands of papers regarding COVID-19. I have been able to calculate an approximate incubation time and the lifetime of the COVID-19 virus, by scrapping through these papers and creating a histogram to find the average of all of the proposed times across thousands of papers.

### Built With
* [Python](https://www.python.org/)



<!-- GETTING STARTED -->
## Getting Started

In order to replicate my results, or to add to this project please follow this setup.

### Prerequisites

Install the following libraries:
* pip
```sh
pip install pandas, numpy, matplotlib, tqdm
```

### Installation

1. Download the CORD-19 Dataset from [https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge/](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge/)
2. Clone the repo
```sh
git clone https://github.com/NoahCristino/CORD-19-Analysis.git
```

<!-- USAGE EXAMPLES -->
## Usage

The project currently scrapes through the entire dataset and converts it into a numpy array. This array then can be searched for keywords such as "incubation" and "life" to find references to these words in the thousands of scholarly papers which are in this data set. I have then sorted and manipulated the results in order to find references to time in days. This data is then processed and turned into a histogram.

#### Keyword "incubation"

![Incubation Histogram](/results/Figure_1.png)

#### Keyword "life"

![Virus Lifetime Histogram](/results/Figure_1.png)

This project needs work, the data searching and the extraction of numbers works, but it can be improved. To find out how to help read: [Contributing](#contributing)

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/NoahCristino/CORD-19-Analysis/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **extremely appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Noah Cristino - [@NoahCristino](https://twitter.com/NoahCristino) - cristinon@protonmail.com

Project Link: [https://github.com/NoahCristino/CORD-19-Analysis/](https://github.com/NoahCristino/CORD-19-Analysis/)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [Kaggle](https://www.kaggle.com/)
## Donations

BTC: 16h1znR18ZKuNrPjtcgYYLVA2wpUupPDcn

Red Cross (Help fight COVID-19): https://www.redcrossblood.org/

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[forks-shield]: https://img.shields.io/github/forks/roshanlam/ReadMeTemplate?style=for-the-badge
[forks-url]: https://github.com/roshanlam/ReadMeTemplate/network/members
[stars-shield]: https://img.shields.io/github/stars/roshanlam/ReadMeTemplate?style=for-the-badge
[stars-url]: https://github.com/roshanlam/ReadMeTemplate/stargazers
[issues-shield]: https://img.shields.io/github/issues/roshanlam/ReadMeTemplate?style=for-the-badge
[issues-url]: https://github.com/roshanlam/ReadMeTemplate/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/roshan-lamichhane
