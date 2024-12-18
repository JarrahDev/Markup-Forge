  var ln = $('.structure > .nav-holder > .left-nav');
  var lnp = $('.structure > .nav-holder > .left-nav-placeholder');
  var appBar = $('.app-bar')[0];
  
  function hideSidebar() {
    ln.animate({left: -ln.outerWidth()}, function() {
      ln.removeClass("in-transition shown").addClass("hidden");
      $('.nav-shield').removeClass("shown");
      $(window).trigger('resize');
    });
    if (window.innerWidth > 998) { 
      $('.content').animate({'margin-left':0}, function(){})
    }
  }
  
  function showSidebar() {
    $('.nav-shield').addClass("shown");
    ln.addClass("shown").removeClass("hidden").css({left: "-100%"}).css({left: -ln.outerWidth()}).animate({left: 0}, function() {
      ln.removeClass("in-transition");
    });
    $(window).trigger('resize');
    if (window.innerWidth > 998) {
      $('.content').animate({'margin-left': ln.outerWidth().toString() + 'px'}, function(){})
    } 
  }
  
  $('.sidebar-toggle, .nav-shield').off('click').on('click', function() { 
    if (ln.is(":visible") || $('.nav-shield').is(".shown")) {
      hideSidebar();
    } else if(!ln.is(":empty")) {
      showSidebar();
    }
  });
  $('.left-nav').off('click').on('click', 'a, button', function() {
    if ($('.nav-shield').is(":visible")) {
      $('.nav-shield').trigger('click');
    }
  });
  
  document.addEventListener('scroll', function() {
    if (appBar.classList.contains('scrolled')) {
      if (window.scrollY === 0) {
        appBar.classList.remove('scrolled')
      }
    }
    else {
      appBar.classList.add('scrolled')
    }
  });

  function addMarginToContent() {
    //check if there is a free banner and set the top margin accordiningly
    let topMargin;
    if ($('#anvil-header').css('display') == 'block') {
      topMargin = appBar.clientHeight + 50
    } else {
      topMargin = appBar.clientHeight
    }
    //the left-nav-placeholder in the designer needs to shift down for the app bar
    lnp.css({'top': appBar.clientHeight.toString() + 'px'})

    //if the window is small
    if (window.innerWidth < 999) {
      //if in Anvil designer
      if (window.anvilInDesigner) {
        //add left margin to content to make room for left-nav or left-nav-placeholder
        $('.content').css({'margin-left': Math.max(ln.outerWidth(), lnp.outerWidth()).toString() + 'px'});
        $('.content').css({'margin-top': appBar.clientHeight.toString() + 'px'})
        ln.css({'top': topMargin.toString() + 'px'})
      } else {
        //if not in Anvil designer, content gets no left margin because left-nav will be a modal overlay
        $('.content').css({'margin-left': '0px'});
        ln.css({'top': '0px'})
        //add top margin to content
        $('.content').css({'margin-top': topMargin.toString() + 'px'});
      }
    } else {
      //if the window is big, add margin to content and left-nav for app bar
      $('.content').css({'margin-top': appBar.clientHeight.toString() + 'px'});
      ln.css({'top': topMargin.toString() + 'px'})
      if (window.anvilInDesigner) {
        //if in the designer, add left margin for either the left-nav or the placeholder
        $('.content').css({'margin-left': Math.max(ln.outerWidth(), lnp.outerWidth()).toString() + 'px'});
      } else {
        //if not in the designer, only add margin for the left-nav because placeholder still has a width outside of designer
        $('.content').css({'margin-left': ln.outerWidth() + 'px'});
      }
    }
  }
  
  addMarginToContent()
  window.addEventListener('resize', addMarginToContent);
 

