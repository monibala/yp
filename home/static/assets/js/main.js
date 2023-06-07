!(function (e) {
    "use strict";
    
    e(window).on("scroll", function () {
        e(this).scrollTop() > 120 ? e(".header-sticky").addClass("is-sticky") : e(".header-sticky").removeClass("is-sticky");
    }),
    e("nav.main-navbar-nav").meanmenu({ meanScreenWidth: "991", meanMenuContainer: ".main-menu-area" }),
    e(".search-button").on("click", function () {
        e(".search-wrapper").toggleClass("is-active");
    }),
    e(".home-slides").owlCarousel({
        items: 1,
        nav: !0,
        dots: !1,
        touchDrag: !0,
        mouseDrag: !0,
        margin: 30,
        autoplay: !0,
        animateOut: "slideOutDown",
        animateIn: "slideInUp",
        smartSpeed: 700,
        loop: !0,
        navText: ["<i class='icofont-rounded-left'></i>", "<i class='icofont-rounded-right'></i>"],
    }),
    e(".popup-video").magnificPopup({ disableOn: 320, type: "iframe", mainClass: "mfp-fade", removalDelay: 160, preloader: !1, fixedContentPos: !1 }),
    e(".achievement-slides").owlCarousel({
        items: 1,
        loop: !0,
        autoplay: !0,
        nav: !0,
        margin: 30,
        animateOut: "slideOutDown",
        animateIn: "slideInRight",
        responsiveClass: !0,
        dots: !1,
        autoplayHoverPause: !0,
        mouseDrag: !0,
        navText: ["<i class='icofont-rounded-left'></i>", "<i class='icofont-rounded-right'></i>"],
    }),
    e(".team-slides").owlCarousel({
        nav: !0,
        dots: !1,
        center: !1,
        touchDrag: !1,
        mouseDrag: !0,
        margin: 30,
        autoplay: !0,
        smartSpeed: 750,
        autoplayHoverPause: !0,
        loop: !0,
        navText: ["<i class='icofont-rounded-left'></i>", "<i class='icofont-rounded-right'></i>"],
        responsive: { 0: { items: 1 }, 576: { items: 2 }, 768: { items: 3 }, 1200: { items: 4 } },
    }),
    e(".news-slides").owlCarousel({
        nav: !0,
        dots: !1,
        center: !1,
        touchDrag: !1,
        mouseDrag: !0,
        autoplay: !0,
        margin: 30,
        smartSpeed: 750,
        autoplayHoverPause: !0,
        loop: !0,
        navText: ["<i class='icofont-rounded-left'></i>", "<i class='icofont-rounded-right'></i>"],
        responsive: { 0: { items: 1 }, 768: { items: 2 }, 1200: { items: 3 } },
    }),
    e(".feedback-slides").owlCarousel({
        nav: !1,
        dots: !0,
        items: 1,
        center: !1,
        touchDrag: !1,
        margin: 30,
        mouseDrag: !0,
        autoplay: !0,
        smartSpeed: 750,
        autoplayHoverPause: !0,
        loop: !0,
        navText: ["<i class='icofont-rounded-left'></i>", "<i class='icofont-rounded-right'></i>"],
    }),
    new WOW().init(),
    e(function () {
        e(".shorting").mixItUp();
    }),
    e(".popup-gallery").magnificPopup({ type: "image", gallery: { enabled: !0 } }),
    e(".news-details-img").owlCarousel({
        nav: !1,
        dots: !1,
        items: 1,
        center: !1,
        touchDrag: !1,
        mouseDrag: !0,
        margin: 30,
        autoplay: !0,
        smartSpeed: 750,
        autoplayHoverPause: !0,
        loop: !0,
        navText: ["<i class='icofont-rounded-left'></i>", "<i class='icofont-rounded-right'></i>"],
    }),
    e(".events-details-img").owlCarousel({
        nav: !1,
        dots: !1,
        items: 1,
        center: !1,
        touchDrag: !1,
        margin: 30,
        mouseDrag: !0,
        autoplay: !0,
        smartSpeed: 750,
        autoplayHoverPause: !0,
        loop: !0,
        navText: ["<i class='icofont-rounded-left'></i>", "<i class='icofont-rounded-right'></i>"],
    }),
    e(function () {
        e(window).on("scroll", function () {
            var o = e(window).scrollTop();
            o > 300 && e(".go-top").fadeIn("slow"), o < 300 && e(".go-top").fadeOut("slow");
        }),
            e(".go-top").on("click", function () {
                e("html, body").animate({ scrollTop: "0" }, 500);
            });
    });

    jQuery(window).on("load", function () {
        e(".preloader-area").fadeOut();
    });

})(jQuery);
