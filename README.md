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
    A Read Me template for your projects!
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

[![Product Name Screen Shot][product-screenshot]](https://example.com)

There are many great README templates available on GitHub, however, I didn't find one that really suit my needs so I created this enhanced one. I want to create a README template so amazing that it'll be the last one you ever need.

Here's why:
* Your time should be focused on creating something amazing. A project that solves a problem and helps others
* You shouldn't be doing the same tasks over and over like creating a README from scratch
* You should element DRY principles to the rest of your life :smile:

Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue.

A list of commonly used resources that I find helpful are listed in the acknowledgements.

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
