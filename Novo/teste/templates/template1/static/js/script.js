(function($) {
  $(document).ready(function() {
  //set the screensize class on load
  var screen_size = checkWindowSize();  
  if(screen_size === 'screen-xs') {
      mobile_carousel();
  }  
  //reset the screensize class on resize
  $( window ).resize(function() {
    var screen_size = checkWindowSize();
    if(screen_size === 'screen-xs') {
      mobile_carousel();
    }
    else {
      $('.mobile-carousel .mobile-carousel-inner').removeClass('carousel-inner');
    }
  });

//Set the Body class based on the screen size  
function checkWindowSize() { 
    var width = $(window).width(), screen_size;
    if(width < 768) {
      screen_size = 'screen-xs'; 
    }
    if(width > 769 && width < 992) {
      screen_size = 'screen-sm'; 
    }
    if(width > 992 && width < 1200) {
      screen_size = 'screen-md'; 
    }
    if (width > 1200 ) {
      screen_size = 'screen-lg'; 
    }
    $(document.body).removeClass('screen-xs screen-sm screen-md screen-lg').addClass(screen_size);
    return screen_size;
}    
//Add the mobile carusel for some of the elements
function mobile_carousel() {
  $('.mobile-carousel').carousel({
    interval: false
  });
  $('.mobile-carousel .mobile-carousel-inner').addClass('carousel-inner');
} 
   
//activate the left right click for mobile     
$('.mobile-carousel .left').click(function() {
  var carsoual_id = $(this).parent().attr('data-carousel-id');
  $('.'+carsoual_id).carousel('prev');
});
$('.mobile-carousel .right').click(function() {
  var carsoual_id = $(this).parent().attr('data-carousel-id');
  $('.'+carsoual_id).carousel('next');
});
  
// END : Mobile carousel functions  


/*--------------------------------------------------------------------------*/
/*------------  Begins : Header / Header Fresh way  ------------------------*/
/*--------------------------------------------------------------------------*/  
$('.front-page nav').removeClass('navbar-scrolled');
$(window).scroll(function() {
  if ($(document).scrollTop() > 514) {
    $('.front-page nav').addClass('navbar-scrolled');
  } else {
    $('.front-page nav').removeClass('navbar-scrolled');
  }
});
/*--------------------------------------------------------------------------*/
/*------------  End : Header / Header Fresh way  ---------------------------*/
/*--------------------------------------------------------------------------*/
 
/*--------------------------------------------------------------------------*/
/*------------  Begins : Stats / stats green sea ---------------------------*/
/*--------------------------------------------------------------------------*/
/* CSS from jquery-asProgress.js library*/ 
$('.progress').asProgress({
            'namespace': 'progress',
            'labelCallback': function(n) {
                      var percentage = this.getPercentage(n);
                      $(this.element).children('.stat-running-number').text(percentage+ "% ");
                      
            },
        }).asProgress('start'); 
/*--------------------------------------------------------------------------*/
/*--------------  Ends : Stats / stats green sea ---------------------------*/
/*--------------------------------------------------------------------------*/		
	$('form.contact-form').validator().on('submit', function (e) {
  if (e.isDefaultPrevented()) {
    
  } else {
e.preventDefault();
    var form = $('form.contact-form');
    var formData = $(form).serialize();
       $.ajax({
    type: 'POST',
    url: $(form).attr('action'),
    data: formData,
    statusCode: {
    400: function() {
      $('form.contact-form .form-message').html("Oops! There was a problem with your submission. Please complete the form and try again.");      
    },
    200: function() {
      $('form.contact-form').addClass('form-submitted');
      $('form.contact-form .contact-form').addClass('hidden');
      $('form.contact-form .submitted-message').removeClass('hidden');      
      $('form.contact-form')[0].reset();
    },
    500: function() {
      $('form.contact-form .form-message').html("Oops! Something went wrong and we couldn't send your message.");
    
    },
    403: function() {
      $('form.contact-form .form-message').html("There was a problem with your submission, please try again.");
   
    },            
  }
})

  }
})

  });
})(jQuery);
