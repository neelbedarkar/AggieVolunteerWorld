    const progressBar = document.querySelector('.progress-bar');
    const main_col = document.querySelector('#maincol');
    const step1 = document.querySelector('#step1');
    const step2 = document.querySelector('#step2');
    const step3 = document.querySelector('#step3');
    const next1 = document.querySelector('#next1');
    const next2 = document.querySelector('#next2');
    const next3 = document.querySelector('#next3');
    const back2 = document.querySelector('#back2');
    const back3 = document.querySelector('#back3');
    const back4 = document.querySelector('#back4');
    const submit = document.querySelector('#submit');

    // Step 1 -> Step 2
    next1.addEventListener('click', () => {
      step1.classList.add('d-none');
      step2.classList.remove('d-none');
      progressBar.style.width = '50%';
      progressBar.setAttribute('aria-valuenow', '50');
    });

    // Step 2 -> Step 1
    back2.addEventListener('click', () => {
      step2.classList.add('d-none');
      step1.classList.remove('d-none');
      progressBar.style.width = '25%';
      progressBar.setAttribute('aria-valuenow', '25');
    });

// Step 2 -> Step 3
    next2.addEventListener('click', () => {
      step2.classList.add('d-none');
      step3.classList.remove('d-none');
      progressBar.style.width = '75%';
      progressBar.setAttribute('aria-valuenow', '75');
    });

    // Step 3 -> Step 2
    back3.addEventListener('click', () => {
      step3.classList.add('d-none');
      step2.classList.remove('d-none');

      progressBar.style.width = '50%';
      progressBar.setAttribute('aria-valuenow', '50');
    });


    // Step 3 -> Step 4
    next3.addEventListener('click', () => {
      step3.classList.add('d-none');
      step4.classList.remove('d-none');
      progressBar.style.width = '99%';
      progressBar.setAttribute('aria-valuenow', '99');
    });

    // Step 3 -> Step 2
    back4.addEventListener('click', () => {
      step4.classList.add('d-none');
      step3.classList.remove('d-none');
      progressBar.style.width = '75%';
      progressBar.setAttribute('aria-valuenow', '75');
    });

    // Submit Form
    submit.addEventListener('click', () => {
      // Handle form submission
    });
const anyCheck = document.getElementById("anyCheck");
const causeSelect = document.getElementById("cause-select");

// add event listener to anyCheck checkbox
anyCheck.addEventListener("change", () => {
  // if anyCheck is checked
  if (anyCheck.checked) {
    // disable all checkboxes within causeSelect div except anyCheck
    const checkboxes = causeSelect.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach((checkbox) => {
      if (checkbox !== anyCheck) {
        checkbox.disabled = true;
      }
    });
  } else {
    // enable all checkboxes within causeSelect div
    const checkboxes = causeSelect.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach((checkbox) => {
      checkbox.disabled = false;
    });
  }
});
function toggleSkip() {
  var skipButton = document.getElementById("skip");

  var formFields = document.querySelectorAll("#step2-form input, #step2-form textarea, #step2-form select");

  if (skipButton.innerHTML === "Skip this Step") {
    skipButton.innerHTML = "Don't Skip This Step";
    formFields.forEach(function(field) {

      field.disabled = true;
           next2.click();
    });
  } else {
    skipButton.innerHTML = "Skip this Step";
    formFields.forEach(function(field) {

     field.disabled =false;
    });
  }

}

var organizations = [
    {
    "org_id": "1",
    "org_name": "Ocean Conservancy",
    "org_city": "Galveston",
    "org_leader": "Jane Doe",
    "org_logo_path": "/static/images/logo1.png",
    "org_description": "Ocean Conservancy is dedicated to protecting the ocean and its inhabitants. We organize beach cleanups, advocate for sustainable fishing practices, and promote ocean conservation worldwide.",
    "org_leader_email": "jane.doe@oceanconservancy.org"
  },
  {
    "org_id": "2",
    "org_name": "High School Tutoring Program",
    "org_city": "Bryan",
    "org_leader": "John Smith",
    "org_logo_path": "/static/images/logo2.png",
    "org_description": "The High School Tutoring Program provides free tutoring services to high school students in the Bryan area. Our volunteers are passionate about education and committed to helping students achieve their academic goals.",
    "org_leader_email": "john.smith@hstutoring.org"
  },
  {
    "org_id": "3",
    "org_name": "Texas A&M Graduate Student Association",
    "org_city": "College Station",
    "org_leader": "Emily Jones",
    "org_logo_path": "/static/images/logo3.png",
    "org_description": "The Texas A&M Graduate Student Association represents the interests of graduate students on campus. We organize social events, provide academic support, and advocate for graduate student rights.",
    "org_leader_email": "emily.jones@gsa.tamu.edu"
  },
  {
    "org_id": "4",
    "org_name": "Texas A&M Diversity, Equity and Inclusion Office",
    "org_city": "College Station",
    "org_leader": "Carlos Rodriguez",
    "org_logo_path": "/static/images/logo4.png",
    "org_description": "The Texas A&M Diversity, Equity and Inclusion Office is committed to creating a welcoming and inclusive environment for all members of the Aggie community. We organize events, provide resources, and advocate for equity and justice.",
    "org_leader_email": "carlos.rodriguez@tamu.edu"
  },
  {
    "org_id": "5",
    "org_name": "Aggie Food Drive",
    "org_city": "College Station",
    "org_leader": "Maria Sanchez",
    "org_logo_path": "/static/images/logo5.png",
    "org_description": "The Aggie Food Drive collects non-perishable food items from the local community and donates them to the Brazos Valley Food Bank. Our volunteers are passionate about fighting hunger and making a difference in the lives of those in need.",
    "org_leader_email": "maria.sanchez@aggiefooddrive.org"
  },
  {
    "org_id": "6",
    "org_name": "Brazos Valley Animal Shelter",
    "org_city": "Longview",
    "org_leader": "David Lee",
    "org_logo_path": "/static/images/logo6.png",
    "org_description": "The Brazos Valley Animal Shelter provides care and shelter for homeless dogs and cats in the Longview area. Our volunteers help with feeding, grooming, and adoption events, and are committed to improving the lives of animals.",
    "org_leader_email": "david.lee@bvshelter.org"
  },
  {
      "org_id": 7,
      "org_name": "Bryan ISD",
      "org_city": "Bryan",
      "org_leader": "John Smith",
      "org_logo_path": "/static/images/logo7.png",
      "org_description": "Bryan ISD is a school district that serves the city of Bryan and parts of College Station. We are committed to providing quality education to our students.",
      "org_leader_email": "john.smith@bryanisd.org"
    },
    {
      "org_id": 8,
      "org_name": "Brazos Valley Food Bank",
      "org_city": "Bryan",
      "org_leader": "Jane Doe",
      "org_logo_path": "/static/images/logo8.png",
      "org_description": "The Brazos Valley Food Bank is a non-profit organization that provides food assistance to families in need in the Brazos Valley area.",
      "org_leader_email": "jane.doe@bvfb.org"
    },
    {
      "org_id": 9,
      "org_name": "Houston Food Bank",
      "org_city": "Houston",
      "org_leader": "Mike Johnson",
      "org_logo_path": "/static/images/logo9.png",
      "org_description": "The Houston Food Bank is the largest food bank in the United States and provides food assistance to families in need in the greater Houston area.",
      "org_leader_email": "mike.johnson@hfb.org"
    },
    {
      "org_id": 10,
      "org_name": "American Cancer Society",
      "org_city": "College Station",
      "org_leader": "Sara Williams",
      "org_logo_path": "/static/images/logo10.png",
      "org_description": "The American Cancer Society is a nationwide non-profit organization that is dedicated to eliminating cancer as a major health problem.",
      "org_leader_email": "sara.williams@cancer.org"
    }
];
// Listen for the keyup event on the search input
$(document).on('input', '.form-control[name="search"]', function() {
  var query = $(this).val().toLowerCase();
  var suggestions = [];

  if (query.length > 0) {
    for (var i = 0; i < organizations.length; i++) {
      var orgName = organizations[i].org_name.toLowerCase();
      if (orgName.indexOf(query) !== -1) {
        suggestions.push(orgName);
      }
    }
  }

  // Display the suggestions in a list group
  var $listGroup = $('.search-suggestions');
  $listGroup.empty(); // Clear the list group
  for (var j = 0; j < suggestions.length; j++) {
    $listGroup.append('<div class="list-group-item">' + suggestions[j] + '</div>'); // Add a suggestion item
  }

  // Show or hide the list group based on whether there are suggestions
  if (suggestions.length > 0) {
    $listGroup.show();
  } else {
    $listGroup.hide();
  }
});

// Hide the list group when the user clicks outside of it
$(document).on('click', function(event) {
  if (!$(event.target).closest('.search-suggestions').length) {
    $('.search-suggestions').hide();
  }
});

$(document).on('click', '.search-suggestions div', function() {
  var $this = $(this);
  var selectedText = $this.text();
  console.log(selectedText);
  $('#search').val(selectedText);
  $('.search-suggestions').hide(); // Hide the suggestions dropdown
});


$( "#search-org" ).on( "submit", function( event ) {

  event.preventDefault();

var query = $('#search').val().toLowerCase();
  var matches = [];

  if (query.length > 0) {
    for (var i = 0; i < organizations.length; i++) {
      var orgName = organizations[i].org_name.toLowerCase();
      if (orgName.indexOf(query) !== -1) {
        matches.push(organizations[i]);
      }
    }
  }

$('.spacerdiv').addClass('d-none');

$('.spacerdivend').removeClass('d-none');

  // Unhide the list group
  $('#resultset').removeClass('d-none');

  // Clear the list group
  $('#resultset').empty();

  // Add each match as a list item
  for (var i = 0; i < matches.length; i++) {
    var match = matches[i];
    var listItemHtml = `
      <li class="list-group-item custom-item" data-bs-org-id="${match.org_id}">
        <div class="row align-items-center justify-content-between">
          <div class="col-2">
            <img src="${match.org_logo_path}" alt="Logo" class="img-fluid rounded" id="opportunity-logo">
          </div>
          <div class="col-6">
            <h5 class="mb-0">${match.org_name}</h5>
            <p class="mb-0">
              <small>${match.org_city}</small>
            </p>
            <p class="mb-0">
              <small>${match.org_leader}</small>
            </p>
          </div>
          <div class="col-4 text-end">
            <button type="button" class="btn btn-warning requestJoinBtn" data-bs-toggle="modal" data-bs-target="#requestToJoinModal"
            data-bs-org-id="${match.org_id}" data-bs-org-name="${match.org_name}">Join</button>
          </div>
        </div>
      </li>
    `;

    $('#resultset').append(listItemHtml);
  }
});

const requestToJoinModal = document.getElementById('requestToJoinModal')
requestToJoinModal.addEventListener('show.bs.modal', event => {
  // Button that triggered the modal
  const button = event.relatedTarget

  const org_name = button.getAttribute('data-bs-org-name')
  const org_id = button.getAttribute('data-bs-org-id')

  const modalHidden = requestToJoinModal.querySelector('#joinOrgID')
  const modalOrgName = requestToJoinModal.querySelector('#orgName')

  modalOrgName.textContent = `${org_name}`
  modalHidden.value = org_id
})

$('#confirmAdd').on('click', function() {
  var modalHiddenVal = requestToJoinModal.querySelector('#joinOrgID').value
  $('#hiddenOrgIdField').val(modalHiddenVal);
  $('#next3').prop('disabled', false);
  $('#search').prop('disabled', true);
  $('.requestJoinBtn').prop('disabled', true);
  $('#searchsubmit').prop('disabled', true);
  $('#toastOrg').text($('#orgName').text());
  $('#requestToJoinModal').modal('hide');
  $('.messagediv').removeClass('d-none')
  var resultset = $('#resultset');
  var matchingItem = resultset.find('[data-bs-org-id="' + modalHiddenVal + '"]');
  resultset.children().not(matchingItem).remove();
  $("#liveToast").toast("show");
});

$('#reset').on('click', function() {
  $('#next3').prop('disabled', true);
  $('#search').prop('disabled', false);
  $('.requestJoinBtn').prop('disabled', false);
  $('#searchsubmit').prop('disabled', false);
  $('.messagediv').addClass('d-none')
  var resultset = $('#resultset');
  resultset.children().remove();

});
