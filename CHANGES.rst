Changelog
=========


1.4.4 (unreleased)
------------------

- Nothing changed yet.


1.4.3 (2023-01-17)
------------------

- SUP-21239: Add cache to speed up users searching in citizen vocabulary
  [laulaz]


1.4.2 (2022-03-28)
------------------

- SUP-17819: Fix help message for user coordinates
  [mpeeters]

- WEB-3411: Color correction for better accessibility
  [thomlamb]


1.4.1 (2020-06-15)
------------------

- WEB-3337: Remove layer restriction for `citizen_control` view since the layer is not yet defined during install of the product
  [mpeeters]

- WEB-3337: Fix an issue with install on multilingual websites with `plone.app.contenttypes` profile
  [mpeeters]


1.4.0 (2020-05-20)
------------------

- WEB-3301: Remove a remaining reference to admin claims dashboard
  [mpeeters]

- WEB-2997: Add email notifications related to citizen or administrator actions
  [mpeeters]

- WEB-3206: Fix an indexation issue where `is_draft` value was set to `False` for working copies
  [mpeeters]


1.3.0 (2020-04-24)
------------------

- WEB-3301: Set the default value for action filter to "Awaiting for approval"
  [mpeeters]

- WEB-3301: Add a new filter on action for admin dashboard
  [mpeeters]

- WEB-3301: Merge admin dashboards into a single dashboard with all contents even contents where no action is required
  [mpeeters]

- WEB-3301: Add `cpskin.citizen.actions` vocabulary to list actions for citizen content
  [mpeeters]

- WEB-3301: Add `is_citizen_content` and `citizen_action` indexes
  [mpeeters]

- WEB-3301: Adapt "state" column on citizen dashboard to display only the current state
  [mpeeters]

- WEB-3301: Fix "online" column value for citizens by adding a new config parameter that define which workflow states are equal to "online"
  [mpeeters]


1.2.3 (2020-04-14)
------------------

- WEB-2937: Add view for administrator to fix broken links for citizen contents
  [mpeeters]

- WEB-2937: Dot not raise an error on citizen dashboard if the link with the draft is broken
  [mpeeters]


1.2.2 (2020-04-07)
------------------

- WEB-2937: Improve cancel view code
  [mpeeters]

- WEB-2937: Add `collective.contact.core` organization content type in tests
  [mpeeters]

- Centralized calls to plone.app.stagingbehavior to prepare the migration to Plone 5
  [mpeeters]

- WEB-2937: LinkIntegrity exceptions must be raised to avoid errors with plone.app.iterate
  [mpeeters]


1.2.1 (2020-03-23)
------------------

- WEB-3245: Fix an issue with claim approval form
  [mpeeters]

- Blackened
  [mpeeters]


1.2.0 (2019-12-11)
------------------

- WEB-2999: Add a reason field for claiming content form and user email on claims administration view
  [mpeeters]

- WEB-3242: Add a css class on dashboard menu items
  [mpeeters]

- WEB-3242: Add a message on propose content view
  [mpeeters]


1.1.0 (2019-12-09)
------------------

- WEB-2937: Fix an issue where some citizen groups are `None` and break security checks
  [mpeeters]

- Add tests for checkout mecanism
  [mpeeters]

- Fix an adapter issue due to order of implementing behavior interfaces
  [mpeeters]

- Add `Event` and `News Item` content types for tests
  [mpeeters]

- Update package dependencies to include plone.app.contenttypes and plone.app.stagingbehavior
  [mpeeters]

- Ensure that security is correctly defined after install
  [mpeeters]

- Adapt french translation
  [mpeeters]

- Add tests for creation folder adapter
  [mpeeters]

- Improve retrievement of creation folder to avoid errors
  [mpeeters]

- Add a view to ensure that security and permissions are correctly defined for citizen related folders
  [mpeeters]

- Add a missing profile dependencies
  [mpeeters]


1.0.5 (2019-02-11)
------------------

- Fix, do not raise exception on execute_under_unrestricted_user, but pass it. There is a starting loop/error with arlon when exception is raised.
  [bsuttor]

- Fix documentation of execute_under_unrestricted_user
  [laulaz]


1.0.4 (2018-11-26)
------------------

- citizen can now add their own image.
  [cboulanger]


1.0.3 (2018-04-15)
------------------

- Remove the unworking redirect on login for citizen users since that can
  not work with overlays
  [mpeeters]


1.0.2 (2018-03-30)
------------------

- Avoid an error on other packages when this package is not installed
  [mpeeters]


1.0.1 (2018-02-26)
------------------

- Fix an encoding issue with user names : #20670
  [mpeeters]


1.0 (2018-01-17)
----------------

- Fix cancel_allowed & checkout_allowed views when user isn't citizen : #20189
  [bsuttor]

- Add an upgrade step to disable role inheritance on citizen draft folders
  : #19973
  [mpeeters]

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
