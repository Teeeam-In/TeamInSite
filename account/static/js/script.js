const enableDisableElements = (elements, isDisabled) => {
    elements.forEach((element) => {
        element.disabled = isDisabled;
    });
};

const enableBtn = document.getElementById('enable-btn');
const disableBtn = document.getElementById('disable-btn');

const addButtonProgLanguage = document.getElementById('addBtnProgrammingLanguage');
const progLanguageInput = document.getElementById('programmingLanguage');
const descriptionProgLanguageInput = document.getElementById('userHardSkillsDescription');
const list = document.getElementById('scrollableList');

const addButtonLanguage = document.getElementById('addBtnLanguages');
const languageInput = document.getElementById('language');
const descriptionLanguageInput = document.getElementById('languageLevel');
const listLanguages = document.getElementById('scrollableListLanguages');

const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
const inputFields = [
    // document.getElementById('fullName'),
    document.getElementById('email'),
    document.getElementById('phoneNumber'),
    document.getElementById('userAddress'),
    document.getElementById('userOccupation'),
    document.getElementById('telegram'),
    document.getElementById('discord'),
    document.getElementById('github'),
    document.getElementById('portfolio'),
    document.getElementById('userHardSkillsDescription'),
    document.getElementById('userDescription'),
    document.getElementById('programmingLanguage'),
    document.getElementById('language'),
    document.getElementById('languageLevel')
];

const buttons = [
    document.getElementById('addBtnLanguages'),
    document.getElementById('addBtnProgrammingLanguage'),
    document.getElementById('btnLanguage'),
    document.getElementById('btnKnowledgeLevel')
];

enableBtn.addEventListener('click', function () {
    enableDisableElements(inputFields, false);
    enableDisableElements(buttons, false);
});

disableBtn.addEventListener('click', function () {
    const info = [
        document.getElementById('email'),
        document.getElementById('phoneNumber'),
        document.getElementById('userAddress'),
        document.getElementById('userOccupation'),
        document.getElementById('telegram'),
        document.getElementById('discord'),
        document.getElementById('github'),
        document.getElementById('portfolio'),
        document.getElementById('userDescription'),
    ]
    const dataObject = {};

    for (let i = 0; i < info.length; i++) {
        dataObject[info[i].getAttribute("name")] = info[i].value;
    }

    $.ajax(
        {
            type: "POST",
            url: "/account/save/",
            data: {
                csrfmiddlewaretoken: csrfToken,
                data: JSON.stringify(dataObject)
            },
            success: function (response) {
                console.log(response);
            },
            error: function (response) {
                console.log(response);
            },
            dataType: "json"
        }
    )

    enableDisableElements(inputFields, true);
    enableDisableElements(buttons, true);

});

function deleteLiElement(el) {
    const listItem = el.parentNode; // get the parent li element
    listItem.parentNode.removeChild(listItem); // remove the li element from the ul list
}

addButtonProgLanguage.addEventListener('click', () => {
    const progLanguage = progLanguageInput.value;
    const progLanguageDescription = descriptionProgLanguageInput.value;

    if (progLanguage && progLanguageDescription) {
        const listItem = document.createElement('li');
        listItem.classList.add('list-group-item', 'deleteBtn', 'mb-2', 'mt-2', 'd-flex', 'justify-content-between', 'align-items-start');
        listItem.innerHTML = `
                                  <div class="ms-2 me-auto">
                                    <div class="fw-bold ">${progLanguage}</div>
                                    ${progLanguageDescription}
                                  </div>
                                  <button onclick="deleteLiElement(this)" style="color: #dc4c64;border: none;" class="cross-btn btn-danger badge rounded-pill">.</button>
                                `;
        list.appendChild(listItem);

        progLanguageInput.value = '';
        descriptionProgLanguageInput.value = '';

        $.ajax(
            {
                type: "POST",
                url: "/account/save/prog_lang/",
                data: {
                    csrfmiddlewaretoken: csrfToken,
                    progLanguage: progLanguage,
                    progLanguageDescription: progLanguageDescription
                },
                success: function (response) {
                    console.log(response);
                },
                error: function (response) {
                    console.log(response);
                },
                dataType: "json"
            }
        )
    }
});


addButtonLanguage.addEventListener('click', () => {
    const language = languageInput.value;
    const languageDescription = descriptionLanguageInput.value;

    if (language && languageDescription) {
        const listItem = document.createElement('li');
        listItem.classList.add('list-group-item', 'mb-2', 'mt-2', 'd-flex', 'justify-content-between', 'align-items-start');
        listItem.innerHTML = `
                                  <div class="ms-2 me-auto">
                                    <div class="fw-bold ">Language: ${language}</div>
                                    Level: ${languageDescription}
                                  </div>
                                  <button onclick="deleteLiElement(this)" style="color: #dc4c64;border: none;" class="cross-btn btn-danger badge rounded-pill">.</button>
                                `;
        listLanguages.appendChild(listItem);

        languageInput.value = '';
        descriptionLanguageInput.value = '';

        $.ajax(
            {
                type: "POST",
                url: "/account/save/lang/",
                data: {
                    csrfmiddlewaretoken: csrfToken,
                    language: language,
                    languageDescription: languageDescription
                },
                success: function (response) {
                    console.log(response);
                },
                error: function (response) {
                    console.log(response);
                },
                dataType: "json"
            }
        )
    }
});