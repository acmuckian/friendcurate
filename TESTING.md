## Table of Contents
- [Performance](#performance)

- [Browser Compatibility](#browser-compatibility)
- [Responsiveness](#responsiveness)

- [Code Validation](#code-validation)

- [Testing](#testing)
  - [Manual Testing](#manual-testing-bdd)
  - [Automated Testing](#automated-testing)
  - [Features Testing](#features-testing)


## Performance

### Google Lighthouse Performance

[Google Lighthouse](https://developers.google.com/web/tools/lighthouse) was used to test the performance of the website.

## Browser Compatibility

| Browser | Responsive |
|---------|------------|
| Chrome  | Yes        |
| Mozilla |    Yes       |
| Safari  |  Yes         |

## Code Validation 

### HTML 

### Javascript 

[JSHint](https://jshint.com/) was used to check the validity of the javascript on comments.js and img_delete.js - comments.js had no errors once /* global bootstrap */ was used so the JSHint warning about bootstrap being an undeclared variable left. This was the same for img_delete.js. 

### CSS 

[Jigsaw CSS](https://jigsaw.w3.org/css-validator/) was used to validate the CSS via a direct upload of the styles.css file. There were no errors and 8 warnings. 

### Python 

[PEP8 CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the Python code by PEP8 standards.

- _contact/models.py_ - all clear, no errors found 
- _contact/forms.py_ - all clear, no errors found
- _contact/views.py_ - all clear, no errors found 

- _img/admin.py_ - all clear, no errors found
- _img/models.py_ - all clear, no errors found 
- _img/forms.py_ - all clear, no errors found
- _img/views.py_ - all clear, no errors found

## Testing 

### Automated Testing 

### Manual Testing

| User Story                                                                                                            | Responsive |
|-----------------------------------------------------------------------------------------------------------------------|------------|
| As a visitor to the site, I can create an account so I can comment on images, edit my comments and add images myself. | Yes        |
| As a user, I can add images that other users can comment on and add to their favourites.                              |  ![screenshot of submit image page](static/images/submitimagepage.png)          |
| As an admin, I can check images and captions, comments to make sure they are okay and up to date and approved.        |            |
| As a user, I can add images to my favourites collection and to be able to view my collection.                         |            |
| As a user, I can sign in to the website so that I can access my account and enjoy customized features and contents.   |            |
| As a user, I can sign out of the website when I finished using it for now.                                            |            |
| As a site owner, I want to encourage visitors to become users of the website.                                         |    ![call to action banner](static/images/calltoaction.png)       |

## Bugs 

| Bug | Fix |
|---------|------------|
| The dropdown bar prevented an email from being required before the submit button was clicked for the newsletter. This bug persisted so the dropdown feature was dropped for the newsletter feature. ![dropdown feature on the newsletter](static/images/Dropdown-bug.png) | The dropdown feature was changed so the form appeared without any dropdown.   |
|  |            |
|   |            |