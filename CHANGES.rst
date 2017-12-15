Changelog
=========


1.0b3 (unreleased)
------------------

- Disable role inheritance on citizen draft folders : #19973
  [mpeeters]

- Add `cleanup_iterate` view to remove broken relations that induce an
  error with iterate behavior : #19972
  [mpeeters]


1.0b2 (2017-12-12)
------------------

- Allow users to update latitude and longitude : #19930
  [mpeeters]


1.0b1 (2017-11-23)
------------------

- Update the description for citizen content creation folder to specify
  that the path should not contains the language folder : #19647
  [mpeeters]


1.0a19 (2017-11-17)
-------------------

- Avoid weird behaviors since citizen users does not have `edit` permission
  : #19647
  [mpeeters]


1.0a18 (2017-11-09)
-------------------

- Fix the redirect on checkout for non citizen users when then does not
  have the `Modify Portal Content` permission : #19492
  [mpeeters]


1.0a17 (2017-10-31)
-------------------

- Fix redirect for citizen users : #18710
  [mpeeters]


1.0a16 (2017-09-12)
-------------------

- Automatically redirect on login citizen users to their dashboards : #18710
  [mpeeters]

- Add a subscriber to remove automatically drafts when the original
  content is removed
  [mpeeters]

- Avoid and error if the original document was removed
  [mpeeters]


1.0a15 (2017-07-17)
-------------------

- Add missing schematas for citizen on organization : #18059
  [laulaz]

- Fix Unicode Decode Error on title column : #18058
  [laulaz]


1.0a14 (2017-06-15)
-------------------

- Add / handle translations for content types & update translations : #17660
  [laulaz]

- Replace fieldsets by divs & remove useless title : #17660
  [laulaz]


1.0a13 (2017-05-31)
-------------------

- Fix error when rendering content table with no working copy
  [laulaz]

- Display content type description in citizen choices and use radios
  [laulaz]


1.0a12 (2017-05-17)
-------------------

- Fix traceback when using iterate on a non-citizen content : #17422
  [laulaz]


1.0a11 (2017-05-17)
-------------------

- Add missing columns in citizen content tables
  [laulaz]

- Change faceted views fields / positions
  [laulaz]

- Remove useless citizen-info-viewlet
  [laulaz]

- Fix special cases generating tracebacks
  [laulaz]

- Never show an empty "Citizen Edition" fieldset
  [laulaz]

- Fix translation
  [laulaz]


1.0a10 (2017-05-08)
-------------------

- Complete refactoring of citizen menu
  [laulaz]

- Fix translations
  [laulaz]


1.0a9 (2017-05-03)
------------------

- Change columns of the citizen contents table
  [laulaz]

- Fix traceback when setting None value
  [laulaz]


1.0a8 (2017-03-01)
------------------

- Refactor actions for citizens : #16438
  [mpeeters]

- Add a viewlet for citizen to access their personal space : #16438
  [mpeeters]

- Add missing css classes for dashboard navigation portlet : #16438
  [mpeeters]

- Update translations : #16438
  [mpeeters]

- Rename the citizen dashboard action and portlet title
  [mpeeters]

- Hide dashboard and undo actions for citizen users
  [mpeeters]


1.0a7 (2016-11-24)
------------------

- Avoid an error for non allowed content type on the draft folder
  [mpeeters]


1.0a6 (2016-11-24)
------------------

- Add a missing filter to allowed claim types
  [mpeeters]


1.0a5 (2016-10-04)
------------------

- Fix the citizen map dashboard query filters
  [mpeeters]

- Add an index to identify geolocated contents
  [mpeeters]

- Fix the index for portal type filter on citizen map dashboard
  [mpeeters]


1.0a4 (2016-10-02)
------------------

- Fix the proposal of new content by citizens
  [mpeeters]


1.0a3 (2016-09-20)
------------------

- Add user map view dashborad for citizen.
  [bsuttor]

- Add the viewlet for content proposal for citizens
  [mpeeters]

- Add user actions for citizen dashboards
  [mpeeters]

- Add the menu portlet for dashboards
  [mpeeters]

- Add dashboards for citizens and administrators
  [mpeeters]

- Add a permission for citizen administration
  [mpeeters]

- Add new indexes for draft and claimed contents
  [mpeeters]

- Add an index to differentiate draft from original
  [mpeeters]

- First implementation for citizen dashboards
  [mpeeters]

- Add plone.app.iterate and plone.app.stagingbehavior to package metadata
  [mpeeters]

- Avoid an error for citizens with the cancel action
  [mpeeters]



1.0a2 (2016-08-31)
------------------

- Automatically add subscribed users to the Citizens group
  [mpeeters]

- Add missing translations
  [mpeeters]

- Fix diff view
  [mpeeters]

- Add link to ask for validation on drafts
  [mpeeters]

- Remove annotations during checkin
  [mpeeters]


1.0a1 (2016-08-24)
------------------

- Initial release.
  [mpeeters]
