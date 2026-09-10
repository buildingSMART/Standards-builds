jQuery(function () {
    var $ = jQuery,
        tmpInput = $('input[name=cookieData]');

    $.cookiesDirective({
        customDialogSelector: tmpInput.attr('data-cookie-customDialogSelector') === 'null' ? null : tmpInput.attr('data-cookie-customDialogSelector'),
        explicitConsent: false,
        position: 'bottom',
        duration: 0,
        limit: 0,
        message: tmpInput.attr('data-cookie-text'),
        fontFamily: 'Arial',
        fontColor: tmpInput.attr('data-cookie-colorText'),
        fontSize: '13px',
        backgroundColor: tmpInput.attr('data-cookie-colorBg'),
        backgroundOpacity: '',
        linkColor: tmpInput.attr('data-cookie-colorLink'),
        underlineLink: tmpInput.attr('data-cookie-underlineLink'),
        textButton: tmpInput.attr('data-cookie-textButton'),
        colorButton: tmpInput.attr('data-cookie-colorButton'),
        animate: tmpInput.attr('data-cookie-customDialogSelector') === 'null'
    });

    tmpInput.remove();
});
