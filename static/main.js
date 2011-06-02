// TODO: consider another format, like:
// RULES = [
//   {for : 'name', type: 'required', onerror: 'missingName'},
//   {...}
// ]

RULES = {
  name: {
     required: {
        onerror: 'missingName'
     },
     limit: {
        limit: 100,
        onerror: 'tooLongName'
     }
  },
  phone: {
     required: {
        onerror: 'missingPhone'
     },
     regexp: {
        regexp: '^(\\d{5,7}|(\\(\\d{3}\\)|\\d{3})\\d{7}|\\+\\d{1,3}(\\(\\d{3}\\)|\\d{3})\\d{7})$',
        onerror: 'incorrectPhone'
     }
  },
  email: {
     required: {
        onerror: 'missingName'
     },
     type: {
        type: 'email',
        onerror: 'incorrectEmail'
     }
  }
}

HANDLERS = {
  limit: function(val, args) {
    if (val.length > args.limit)
      return args.onerror;
  },
  required: function(val, args) {
    if (!val)
      return args.onerror;
  },
  regexp: function(val, args) {
    if (!val.match(new RegExp(args.regexp)))
      return args.onerror;
  },
  type: function(val, args) {
    var regexp = {
      email: /^[-.\w]+@(?:[a-z\d][-a-z\d]+\.)+[a-z]{2,6}$/
    }[args.type];
    if (!val.match(regexp))
      return args.onerror;
  }
}

function validateInput(name) {
  var val = document.getElementsByName(name)[0].value,
      rule,
      error;

  val = val.replace(/^\s*/, '').replace(/\s*$/, '');
  for (rule in RULES[name]) {
    error = HANDLERS[rule](val, RULES[name][rule]);
    if (error) {
      showError(error, name);
      return false;
    }
  }
  return true;
}

function showError(error, name) {
  // argument 'name' is not necessary at this point
  // it just gives more possibilities
  document.getElementsByName(name)[0].focus();
  alert(error);
};

function bindHandlerToEl(name, event) {
  var el = document.getElementsByName(name)[0];
  if (el.nodeName == 'FORM') {
    el[event] = function () {
      for (var field in RULES) {
        if (el.document.getElementsByName(field)[0] && !validateInput(name)) { 
          return false;
        };
      };
    };
  } else {
    el[event] = function () {
      return validateInput(this.name);
    };
  };
};

(function() {
  bindHandlerToEl('form', 'onsubmit');
  var inputs = 'name phone email'.split(' ');
  for (var i in inputs) {
    bindHandlerToEl(inputs[i], 'onblur');
  };
})();
