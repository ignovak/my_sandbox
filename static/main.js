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
      // add typical regexps here
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
    if (error = HANDLERS[rule](val, RULES[name][rule])) {
      return showError(error);
    }
  }
  return true;
}

// implement way to show message to user
// consider passing field's name or id for more options
function showError(error) {
  alert(error);
  return false;
};

function bindHandlerToEl(name, event) {
  document.getElementsByName(name)[0][event] = function () {
    if (this.nodeName == 'FORM') {
      for (var field in RULES) {
        if (!validateInput(field)) { 
          return false;
        };
      };
    } else {
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
