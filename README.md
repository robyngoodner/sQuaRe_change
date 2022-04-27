[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<h3 align="center">sQuaRe change</h3>

  <p align="center">
    An app that enables QR-code driven microtransactions between donors and receivers of donations, which can then be redeemed at participating grocery stores.
    <br />
    <a href="https://github.com/robyngoodner/sQuaRe_change"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://square-change.herokuapp.com/">View Live</a>
    ·
    <a href="https://github.com/robyngoodner/sQuaRe_change/issues">Report Bug</a>
    ·
    <a href="https://github.com/robyngoodner/sQuaRe_change/issues">Request Feature</a>
  </p>
  <strong>Vision and name credit: The illustrious Oliver Thomas</strong>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    <li><a href="#user_stories">User Stories</a></li>
    <li><a href="#erd">ERD</a></li>
    <li><a href="#wireframes">Wire frames</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
![Screen Shot 2022-04-27 at 7 05 56 PM](https://user-images.githubusercontent.com/90972554/165645551-be58ac70-da3e-4fbc-a99e-ea06a165ba29.png)

sQuaRe change was designed to bridge the gap between people who need help and people who are interested in giving it, but who no longer have an easy way to do so. sQuaRe change enables you to quickly donate small amounts of money to others by scanning their QR code. The money you have donated is redeemable only at participating local grocery stores. sQuaRe change also enables participating stores to match your donation, making your small contribution go even further. Register for an account today in order to: donate, recieve, help those without smart phones sign up, or register as a local grocery store.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [Python](https://python.org/)
* [Javascript](https://javascript.com)
* [Django](https://djangoproject.com)
* [JQuery](https://jquery.com)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right"><a href="#top">back to top</a></p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right"><a href="#top">back to top</a></p>



<!-- CONTACT -->
## Contact

Robyn Goodner - robyn.goodner@gmail.com

Project Link: [https://github.com/robyngoodner/sQuaRe_change](https://github.com/robyngoodner/sQuaRe_change)

<p align="right"><a href="#top">back to top</a></p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Oliver Thomas](https://github.com/othomasprime)

<p align="right"><a href="#top">back to top</a></p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/robyngoodner/sQuaRe_change.svg?style=for-the-badge
[contributors-url]: https://github.com/robyngoodner/sQuaRe_change/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/robyngoodner/sQuaRe_change.svg?style=for-the-badge
[forks-url]: https://github.com/robyngoodner/sQuaRe_change/network/members
[stars-shield]: https://img.shields.io/github/stars/robyngoodner/sQuaRe_change.svg?style=for-the-badge
[stars-url]: https://github.com/robyngoodner/sQuaRe_change/stargazers
[issues-shield]: https://img.shields.io/github/issues/robyngoodner/sQuaRe_change.svg?style=for-the-badge
[issues-url]: https://github.com/robyngoodner/sQuaRe_change/issues
[license-shield]: https://img.shields.io/github/license/robyngoodner/sQuaRe_change.svg?style=for-the-badge
[license-url]: https://github.com/robyngoodner/sQuaRe_change/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/robyn-goodner
[product-screenshot]: images/screenshot.png


## User_Stories
- As a user, I want to create an account.
- As a user, I want to be able to select whether I am a donor, receiver, store, or helper.
- As a user, I want to see a random helping hand article at the bottom of the login page.
- As a user, I want to login.
- As a helper, I want to be able to access my helper account only after having been verified to have an official helper email address. (working for a shelter, vetted volunteers, etc)
- As a helper, I want to be able to set up receiver's accounts.
- As a helper, I want to be able to enter a receiver's identifying information in order to print their QR code for them.
- As a donor, I want to be able to scan a receiver's QR code and donate money to their pool.
- As a donor, I want to be able to see the transactions of what I have donated in the past.
- As a donor, I want to see spotlights of various receivers on my home page, in order to encourage me to donate.
- As a donor, I want to set standard sizes for the donations that I will give when I sign up.
- As a donor, I want to edit the standard sizes of donations that I have available.
- As a donor, I want to print a yearly transaction report of my donations.
- As a non-user donor, I want to be able to scan a QR code and donate through apple wallet(?) without signing in.
- As a receiver, I want to present my QR code in order to receive donations.
- As a receiver, I want to sign up with a unique identifier instead of only an email address.
- As a receiver, I want to scan a grocery store's QR code in order to redeem my donations.
- As a receiver, I want to see the history of the donations I have received.
- As a grocery store, I want to scan the QR code of a receiver to help them pay for their purchase.
- As a grocery store, I want to see a history of the transactions at my store.
- As a grocery store, I want to be able to automatically match donations.
- As a grocery store, I want to print a yearly transaction report of my donations.
- As a grocery store, I want to enter the identifying information of a receiver to help them pay for their purchase.

## ERD
![Screen Shot 2022-04-16 at 3 07 16 PM](https://user-images.githubusercontent.com/90972554/163688246-d578e20a-aed6-4d00-8b09-231b7847b712.png)

## Wire_Frames
### Home Page, not logged in:
![image](https://user-images.githubusercontent.com/90972554/163688857-ab5129b0-cfab-438a-b390-d89cd6884c5e.png)
### Registration:
![image](https://user-images.githubusercontent.com/90972554/163688864-6e83b319-b6fb-4124-92ac-3873d33db750.png)
### Upon registration: Donor view:
![image](https://user-images.githubusercontent.com/90972554/163688463-adccb8e7-fd4d-40fe-bfb8-de801fa0cca4.png)
### Upon registration: Receiver view:
![image](https://user-images.githubusercontent.com/90972554/163688474-7fbf46ce-af3f-45bd-b827-ba616d283d5b.png)
### Upon registration: Store view:
![image](https://user-images.githubusercontent.com/90972554/163688482-1c16c789-01fa-41ef-af50-7f2ac4fe444b.png)
### Upon registration: Helper view:
![image](https://user-images.githubusercontent.com/90972554/163688059-ba53832e-4656-409c-ba12-0cd606ccd8a5.png)
### Upon login, donator view:
![image](https://user-images.githubusercontent.com/90972554/163688499-1a366c3c-420b-4a95-8486-5f7d348f0160.png)
### Upon login, receiver view:
![image](https://user-images.githubusercontent.com/90972554/163688505-af20554e-53b9-405c-8960-b65fa3e09985.png)
### Upon login, store view:
![image](https://user-images.githubusercontent.com/90972554/163688183-c43c878f-437b-425d-8274-9dff90dbc6ae.png)
### Upon login, helper view:
![image](https://user-images.githubusercontent.com/90972554/163688196-749ce9b1-8e69-40c5-aaa8-9eb5173cec4d.png)




