register(QUICKREPORT,
         id = 'NumberOfAncestorsQuickview',
         name = _("Number of ancestors"),
         description = _("Shows the number of ancestores of the current person."),
         version = '1.0.0',
         gramps_target_version = "5.1",
         status = STABLE,
         fname = 'NumberOfAncestorsQuickview.py',
         authors = ["Matthias Kemmer"],
         authors_email = ["matt.familienforschung@gmail.com"],
         category = CATEGORY_QR_PERSON,
         runfunc = 'run')
