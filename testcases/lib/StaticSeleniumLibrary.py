# -*- coding=utf-8 -*-
"""Automatically generated static reference for dynamic CustomSelenuimLibrary"""
# pylint: skip-file
from robot.api.deco import keyword

try:
    from SeleniumLibrary import SeleniumLibrary
    from SeleniumLibrary.keywords.alert import AlertKeywords
    from SeleniumLibrary.keywords.window import WindowKeywords
    from SeleniumLibrary.keywords.cookie import CookieKeywords
    from SeleniumLibrary.keywords.browsermanagement import BrowserManagementKeywords
    from SeleniumLibrary.keywords.screenshot import ScreenshotKeywords
    from SeleniumLibrary.keywords.waiting import WaitingKeywords
    from SeleniumLibrary.keywords.tableelement import TableElementKeywords
    from SeleniumLibrary.keywords.runonfailure import RunOnFailureKeywords
    from SeleniumLibrary.keywords.formelement import FormElementKeywords
    from SeleniumLibrary.keywords.frames import FrameKeywords
    from SeleniumLibrary.keywords.javascript import JavaScriptKeywords
    from SeleniumLibrary.keywords.element import ElementKeywords
    from SeleniumLibrary.keywords.selectelement import SelectElementKeywords
except SyntaxError:
    class SeleniumLibrary(object):
        """STUB for py2 RIDE"""
        def __init__(self, *args, **kwargs):
            pass


# noinspection PyArgumentList
class StaticCustomSeleniumLibrary(SeleniumLibrary):
    """SeleniumLibrary is a web testing library for Robot Framework.

    This document explains how to use keywords provided by SeleniumLibrary.
    For information about installation, support, and more, please visit the
    [https://github.com/robotframework/SeleniumLibrary|project pages].
    For more information about Robot Framework, see http://robotframework.org.

    SeleniumLibrary uses the Selenium WebDriver modules internally to
    control a web browser. See http://seleniumhq.org for more information
    about Selenium in general and SeleniumLibrary README.rst
    [https://github.com/robotframework/SeleniumLibrary#browser-drivers|Browser drivers chapter]
    for more details about WebDriver binary installation.

    %TOC%

    = Locating elements =

    All keywords in SeleniumLibrary that need to interact with an element
    on a web page take an argument typically named ``locator`` that specifies
    how to find the element. Most often the locator is given as a string
    using the locator syntax described below, but `using WebElements` is
    possible too.

    == Locator syntax ==

    SeleniumLibrary supports finding elements based on different strategies
    such as the element id, XPath expressions, or CSS selectors. The strategy
    can either be explicitly specified with a prefix or the strategy can be
    implicit.

    === Default locator strategy ===

    By default, locators are considered to use the keyword specific default
    locator strategy. All keywords support finding elements based on ``id``
    and ``name`` attributes, but some keywords support additional attributes
    or other values that make sense in their context. For example, `Click
    Link` supports the ``href`` attribute and the link text and addition
    to the normal ``id`` and ``name``.

    Examples:

    | `Click Element` | example | # Match based on ``id`` or ``name``.            |
    | `Click Link`    | example | # Match also based on link text and ``href``.   |
    | `Click Button`  | example | # Match based on ``id``, ``name`` or ``value``. |

    If a locator accidentally starts with a prefix recognized as `explicit
    locator strategy` or `implicit XPath strategy`, it is possible to use
    the explicit ``default`` prefix to enable the default strategy.

    Examples:

    | `Click Element` | name:foo         | # Find element with name ``foo``.               |
    | `Click Element` | default:name:foo | # Use default strategy with value ``name:foo``. |
    | `Click Element` | //foo            | # Find element using XPath ``//foo``.           |
    | `Click Element` | default: //foo   | # Use default strategy with value ``//foo``.    |

    === Explicit locator strategy ===

    The explicit locator strategy is specified with a prefix using either
    syntax ``strategy:value`` or ``strategy=value``. The former syntax
    is preferred because the latter is identical to Robot Framework's
    [http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#named-argument-syntax|
    named argument syntax] and that can cause problems. Spaces around
    the separator are ignored, so ``id:foo``, ``id: foo`` and ``id : foo``
    are all equivalent.

    Locator strategies that are supported by default are listed in the table
    below. In addition to them, it is possible to register `custom locators`.

    | = Strategy = |          = Match based on =         |         = Example =            |
    | id           | Element ``id``.                     | ``id:example``                 |
    | name         | ``name`` attribute.                 | ``name:example``               |
    | identifier   | Either ``id`` or ``name``.          | ``identifier:example``         |
    | class        | Element ``class``.                  | ``class:example``              |
    | tag          | Tag name.                           | ``tag:div``                    |
    | xpath        | XPath expression.                   | ``xpath://div[@id="example"]`` |
    | css          | CSS selector.                       | ``css:div#example``            |
    | dom          | DOM expression.                     | ``dom:document.images[5]``     |
    | link         | Exact text a link has.              | ``link:The example``           |
    | partial link | Partial link text.                  | ``partial link:he ex``         |
    | sizzle       | Sizzle selector deprecated.         | ``sizzle:div.example``         |
    | jquery       | jQuery expression.                  | ``jquery:div.example``         |
    | default      | Keyword specific default behavior.  | ``default:example``            |

    See the `Default locator strategy` section below for more information
    about how the default strategy works. Using the explicit ``default``
    prefix is only necessary if the locator value itself accidentally
    matches some of the explicit strategies.

    Different locator strategies have different pros and cons. Using ids,
    either explicitly like ``id:foo`` or by using the `default locator
    strategy` simply like ``foo``, is recommended when possible, because
    the syntax is simple and locating elements by id is fast for browsers.
    If an element does not have an id or the id is not stable, other
    solutions need to be used. If an element has a unique tag name or class,
    using ``tag``, ``class`` or ``css`` strategy like ``tag:h1``,
    ``class:example`` or ``css:h1.example`` is often an easy solution. In
    more complex cases using XPath expressions is typically the best
    approach. They are very powerful but a downside is that they can also
    get complex.

    Examples:

    | `Click Element` | id:foo                      | # Element with id 'foo'. |
    | `Click Element` | css:div#foo h1              | # h1 element under div with id 'foo'. |
    | `Click Element` | xpath: //div[@id="foo"]//h1 | # Same as the above using XPath, not CSS. |
    | `Click Element` | xpath: //*[contains(text(), "example")] | # Element containing text 'example'. |

    *NOTE:*

    - The ``strategy:value`` syntax is only supported by SeleniumLibrary 3.0
      and newer.
    - Using the ``sizzle`` strategy or its alias ``jquery`` requires that
      the system under test contains the jQuery library.
    - Prior to SeleniumLibrary 3.0, table related keywords only supported
      ``xpath``, ``css`` and ``sizzle/jquery`` strategies.

    === Implicit XPath strategy ===

    If the locator starts with ``//`` or ``(//``, the locator is considered
    to be an XPath expression. In other words, using ``//div`` is equivalent
    to using explicit ``xpath://div``.

    Examples:

    | `Click Element` | //div[@id="foo"]//h1 |
    | `Click Element` | (//div)[2]           |

    The support for the ``(//`` prefix is new in SeleniumLibrary 3.0.

    == Using WebElements ==

    In addition to specifying a locator as a string, it is possible to use
    Selenium's WebElement objects. This requires first getting a WebElement,
    for example, by using the `Get WebElement` keyword.

    | ${elem} =       | `Get WebElement` | id:example |
    | `Click Element` | ${elem}          |            |

    == Custom locators ==

    If more complex lookups are required than what is provided through the
    default locators, custom lookup strategies can be created. Using custom
    locators is a two part process. First, create a keyword that returns
    a WebElement that should be acted on:

    | Custom Locator Strategy | [Arguments] | ${browser} | ${locator} | ${tag} | ${constraints} |
    |   | ${element}= | Execute Javascript | return window.document.getElementById('${locator}'); |
    |   | [Return] | ${element} |

    This keyword is a reimplementation of the basic functionality of the
    ``id`` locator where ``${browser}`` is a reference to a WebDriver
    instance and ``${locator}`` is the name of the locator strategy. To use
    this locator, it must first be registered by using the
    `Add Location Strategy` keyword:

    | `Add Location Strategy` | custom | Custom Locator Strategy |

    The first argument of `Add Location Strategy` specifies the name of
    the strategy and it must be unique. After registering the strategy,
    the usage is the same as with other locators:

    | `Click Element` | custom:example |

    See the `Add Location Strategy` keyword for more details.

    = Browser and Window =

    There is different conceptual meaning when SeleniumLibrary talks
    about windows or browsers. This chapter explains those differences.

    == Browser ==

    When `Open Browser` or `Create WebDriver` keyword is called, it
    will create a new Selenium WebDriver instance by using the
    [https://www.seleniumhq.org/docs/03_webdriver.jsp|Selenium WebDriver]
    API. In SeleniumLibrary terms, a new browser is created. It is
    possible to start multiple independent browsers (Selenium Webdriver
    instances) at the same time, by calling `Open Browser` or
    `Create WebDriver` multiple times. These browsers are usually
    independent of each other and do not share data like cookies,
    sessions or profiles. Typically when the browser starts, it
    creates a single window which is shown to the user.

    == Window ==

    Windows are the part of a browser that loads the web site and presents
    it to the user. All content of the site is the content of the window.
    Windows are children of a browser. In SeleniumLibrary browser is a
    synonym for WebDriver instance. One browser may have multiple
    windows. Windows can appear as tabs, as separate windows or pop-ups with
    different position and size. Windows belonging to the same browser
    typically share the sessions detail, like cookies. If there is a
    need to separate sessions detail, example login with two different
    users, two browsers (Selenium WebDriver instances) must be created.
    New windows can be opened example by the application under test or
    by example `Execute Javascript` keyword:

    | `Execute Javascript`    window.open()    # Opens a new window with location about:blank

    The example below opens multiple browsers and windows,
    to demonstrate how the different keywords can be used to interact
    with browsers, and windows attached to these browsers.

    Structure:
    | BrowserA
    |            Window 1  (location=https://robotframework.org/)
    |            Window 2  (location=https://robocon.io/)
    |            Window 3  (location=https://github.com/robotframework/)
    |
    | BrowserB
    |            Window 1  (location=https://github.com/)

    Example:
    | `Open Browser`       | https://robotframework.org         | ${BROWSER}       | alias=BrowserA   | # BrowserA with first window is opened.                                       |
    | `Execute Javascript` | window.open()                      |                  |                  | # In BrowserA second window is opened.                                        |
    | `Switch Window`      | locator=NEW                        |                  |                  | # Switched to second window in BrowserA                                       |
    | `Go To`              | https://robocon.io                 |                  |                  | # Second window navigates to robocon site.                                    |
    | `Execute Javascript` | window.open()                      |                  |                  | # In BrowserA third window is opened.                                         |
    | ${handle}            | `Switch Window`                    | locator=NEW      |                  | # Switched to third window in BrowserA                                        |
    | `Go To`              | https://github.com/robotframework/ |                  |                  | # Third windows goes to robot framework github site.                          |
    | `Open Browser`       | https://github.com                 | ${BROWSER}       | alias=BrowserB   | # BrowserB with first windows is opened.                                      |
    | ${location}          | `Get Location`                     |                  |                  | # ${location} is: https://www.github.com                                      |
    | `Switch Window`      | ${handle}                          | browser=BrowserA |                  | # BrowserA second windows is selected.                                        |
    | ${location}          | `Get Location`                     |                  |                  | # ${location} = https://robocon.io/                                           |
    | @{locations 1}       | `Get Locations`                    |                  |                  | # By default, lists locations under the currectly active browser (BrowserA).   |
    | @{locations 2}       | `Get Locations`                    |  browser=ALL     |                  | # By using browser=ALL argument keyword list all locations from all browsers. |

    The above example, @{locations 1} contains the following items:
    https://robotframework.org/, https://robocon.io/ and
    https://github.com/robotframework/'. The @{locations 2}
    contains the following items: https://robotframework.org/,
    https://robocon.io/, https://github.com/robotframework/'
    and 'https://github.com/.

    = Timeouts, waits, and delays =

    This section discusses different ways how to wait for elements to
    appear on web pages and to slow down execution speed otherwise.
    It also explains the `time format` that can be used when setting various
    timeouts, waits, and delays.

    == Timeout ==

    SeleniumLibrary contains various keywords that have an optional
    ``timeout`` argument that specifies how long these keywords should
    wait for certain events or actions. These keywords include, for example,
    ``Wait ...`` keywords and keywords related to alerts. Additionally
    `Execute Async Javascript`. Although it does not have ``timeout``,
    argument, uses a timeout to define how long asynchronous JavaScript
    can run.

    The default timeout these keywords use can be set globally either by
    using the `Set Selenium Timeout` keyword or with the ``timeout`` argument
    when `importing` the library. See `time format` below for supported
    timeout syntax.

    == Implicit wait ==

    Implicit wait specifies the maximum time how long Selenium waits when
    searching for elements. It can be set by using the `Set Selenium Implicit
    Wait` keyword or with the ``implicit_wait`` argument when `importing`
    the library. See [https://www.seleniumhq.org/docs/04_webdriver_advanced.jsp|
    Selenium documentation] for more information about this functionality.

    See `time format` below for supported syntax.

    == Selenium speed ==

    Selenium execution speed can be slowed down globally by using `Set
    Selenium speed` keyword. This functionality is designed to be used for
    demonstrating or debugging purposes. Using it to make sure that elements
    appear on a page is not a good idea. The above-explained timeouts
    and waits should be used instead.

    See `time format` below for supported syntax.

    == Time format ==

    All timeouts and waits can be given as numbers considered seconds
    (e.g. ``0.5`` or ``42``) or in Robot Framework's time syntax
    (e.g. ``1.5 seconds`` or ``1 min 30 s``). For more information about
    the time syntax see the
    [http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#time-format|Robot Framework User Guide].

    = Run-on-failure functionality =

    SeleniumLibrary has a handy feature that it can automatically execute
    a keyword if any of its own keywords fails. By default, it uses the
    `Capture Page Screenshot` keyword, but this can be changed either by
    using the `Register Keyword To Run On Failure` keyword or with the
    ``run_on_failure`` argument when `importing` the library. It is
    possible to use any keyword from any imported library or resource file.

    The run-on-failure functionality can be disabled by using a special value
    ``NOTHING`` or anything considered false (see `Boolean arguments`)
    such as ``NONE``.

    = Boolean arguments =

    Some keywords accept arguments that are handled as Boolean values true or
    false. If such an argument is given as a string, it is considered false if
    it is either empty or case-insensitively equal to ``false``, ``no``, ``off``,
     ``0`` or ``none``. Other strings are considered true regardless of their value and
    other argument types are tested using the same
    [https://docs.python.org/3/library/stdtypes.html#truth-value-testing|rules as in Python].

    True examples:

    | `Set Screenshot Directory` | ${RESULTS} | persist=True    | # Strings are generally true.    |
    | `Set Screenshot Directory` | ${RESULTS} | persist=yes     | # Same as the above.             |
    | `Set Screenshot Directory` | ${RESULTS} | persist=${TRUE} | # Python True is true.           |
    | `Set Screenshot Directory` | ${RESULTS} | persist=${42}   | # Numbers other than 0 are true. |

    False examples:

    | `Set Screenshot Directory` | ${RESULTS} | persist=False    | # String false is false.        |
    | `Set Screenshot Directory` | ${RESULTS} | persist=no       | # Also string no is false.      |
    | `Set Screenshot Directory` | ${RESULTS} | persist=NONE     | # String NONE is false.         |
    | `Set Screenshot Directory` | ${RESULTS} | persist=${EMPTY} | # Empty string is false.        |
    | `Set Screenshot Directory` | ${RESULTS} | persist=${FALSE} | # Python False is false.        |
    | `Set Screenshot Directory` | ${RESULTS} | persist=${NONE}  | # Python None is false.         |

    Note that prior to SeleniumLibrary 3.0, all non-empty strings, including
    ``false``, ``no`` and ``none``, were considered true. Starting from
    SeleniumLibrary 4.0, strings ``0`` and ``off`` are considered as false.

    = EventFiringWebDriver =

    The SeleniumLibrary offers support for
    [https://seleniumhq.github.io/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.event_firing_webdriver.html#module-selenium.webdriver.support.event_firing_webdriver|EventFiringWebDriver].
    See the Selenium and SeleniumLibrary
    [https://github.com/robotframework/SeleniumLibrary/blob/master/docs/extending/extending.rst#EventFiringWebDriver|EventFiringWebDriver support]
    documentation for further details.

    EventFiringWebDriver is new in SeleniumLibrary 4.0

    = Thread support =

    SeleniumLibrary is not thread-safe. This is mainly due because the underlying
    [https://github.com/SeleniumHQ/selenium/wiki/Frequently-Asked-Questions#q-is-webdriver-thread-safe|
    Selenium tool is not thread-safe] within one browser/driver instance.
    Because of the limitation in the Selenium side, the keywords or the
    API provided by the SeleniumLibrary is not thread-safe.

    = Plugins =

    SeleniumLibrary offers plugins as a way to modify and add library keywords and modify some of the internal
    functionality without creating a new library or hacking the source code. See
    [https://github.com/robotframework/SeleniumLibrary/blob/master/docs/extending/extending.rst#Plugins|plugin API]
    documentation for further details.

    Plugin API is new SeleniumLibrary 4.0
    """

    ROBOT_LIBRARY_VERSION = "4.3.0"
    ROBOT_LIBRARY_SCOPE = "global"

    def __init__(self, timeout=5.0, implicit_wait=0.0, run_on_failure='Capture Page Screenshot', screenshot_root_directory=None, plugins=None, event_firing_webdriver=None):
        super().__init__(timeout, implicit_wait, run_on_failure, screenshot_root_directory, plugins, event_firing_webdriver)
        self.keywords = {}
        self.customseleniumlibrary = SeleniumLibrary(timeout, implicit_wait, run_on_failure, screenshot_root_directory, plugins, event_firing_webdriver)
        try:
            self.browsermanagementkeywords = BrowserManagementKeywords(self)
            self.selectelementkeywords = SelectElementKeywords(self)
            self.formelementkeywords = FormElementKeywords(self)
            self.alertkeywords = AlertKeywords(self)
            self.framekeywords = FrameKeywords(self)
            self.waitingkeywords = WaitingKeywords(self)
            self.screenshotkeywords = ScreenshotKeywords(self)
            self.javascriptkeywords = JavaScriptKeywords(self)
            self.elementkeywords = ElementKeywords(self)
            self.runonfailurekeywords = RunOnFailureKeywords(self)
            self.cookiekeywords = CookieKeywords(self)
            self.tableelementkeywords = TableElementKeywords(self)
            self.windowkeywords = WindowKeywords(self)
        except Exception:
            pass
        self.add_library_components([self.customseleniumlibrary])

    @keyword(name="Alert Should Be Present")
    def alert_should_be_present(self, text='', action='ACCEPT', timeout=None):
        """Verifies that an alert is present and by default, accepts it.

        Fails if no alert is present. If ``text`` is a non-empty string,
        then it is used to verify alert's message. The alert is accepted
        by default, but that behavior can be controlled by using the
        ``action`` argument same way as with `Handle Alert`.

        ``timeout`` specifies how long to wait for the alert to appear.
        If it is not given, the global default `timeout` is used instead.

        ``action`` and ``timeout`` arguments are new in SeleniumLibrary 3.0.
        In earlier versions, the alert was always accepted and a timeout was
        hardcoded to one second.
        """
        return self.alertkeywords.alert_should_be_present(text, action, timeout)

    @keyword(name="Alert Should Not Be Present")
    def alert_should_not_be_present(self, action='ACCEPT', timeout=0):
        """Verifies that no alert is present.

        If the alert actually exists, the ``action`` argument determines
        how it should be handled. By default, the alert is accepted, but
        it can be also dismissed or left open the same way as with the
        `Handle Alert` keyword.

        ``timeout`` specifies how long to wait for the alert to appear.
        By default, is not waited for the alert at all, but a custom time can
        be given if alert may be delayed. See the `time format` section
        for information about the syntax.

        New in SeleniumLibrary 3.0.
        """
        return self.alertkeywords.alert_should_not_be_present(action, timeout)

    @keyword(name="Handle Alert")
    def handle_alert(self, action='ACCEPT', timeout=None):
        """Handles the current alert and returns its message.

        By default, the alert is accepted, but this can be controlled
        with the ``action`` argument that supports the following
        case-insensitive values:

        - ``ACCEPT``: Accept the alert i.e. press ``Ok``. Default.
        - ``DISMISS``: Dismiss the alert i.e. press ``Cancel``.
        - ``LEAVE``: Leave the alert open.

        The ``timeout`` argument specifies how long to wait for the alert
        to appear. If it is not given, the global default `timeout` is used
        instead.

        Examples:
        | Handle Alert |                |       | # Accept alert.  |
        | Handle Alert | action=DISMISS |       | # Dismiss alert. |
        | Handle Alert | timeout=10 s   |       | # Use custom timeout and accept alert.  |
        | Handle Alert | DISMISS        | 1 min | # Use custom timeout and dismiss alert. |
        | ${message} = | Handle Alert   |       | # Accept alert and get its message.     |
        | ${message} = | Handle Alert   | LEAVE | # Leave alert open and get its message. |

        New in SeleniumLibrary 3.0.
        """
        return self.alertkeywords.handle_alert(action, timeout)

    @keyword(name="Input Text Into Alert")
    def input_text_into_alert(self, text, action='ACCEPT', timeout=None):
        """Types the given ``text`` into an input field in an alert.

        The alert is accepted by default, but that behavior can be controlled
        by using the ``action`` argument same way as with `Handle Alert`.

        ``timeout`` specifies how long to wait for the alert to appear.
        If it is not given, the global default `timeout` is used instead.

        New in SeleniumLibrary 3.0.
        """
        return self.alertkeywords.input_text_into_alert(text, action, timeout)

    @keyword(name="Close All Browsers")
    def close_all_browsers(self):
        """Closes all open browsers and resets the browser cache.

        After this keyword, new indexes returned from `Open Browser` keyword
        are reset to 1.

        This keyword should be used in test or suite teardown to make sure
        all browsers are closed.
        """
        return self.browsermanagementkeywords.close_all_browsers()

    @keyword(name="Close Browser")
    def close_browser(self):
        """Closes the current browser."""
        return self.browsermanagementkeywords.close_browser()

    @keyword(name="Create Webdriver")
    def create_webdriver(self, driver_name, alias=None, kwargs={}, **init_kwargs):
        """Creates an instance of Selenium WebDriver.

        Like `Open Browser`, but allows passing arguments to the created
        WebDriver instance directly. This keyword should only be used if
        the functionality provided by `Open Browser` is not adequate.

        ``driver_name`` must be a WebDriver implementation name like Firefox,
        Chrome, Ie, Opera, Safari, PhantomJS, or Remote.

        The initialized WebDriver can be configured either with a Python
        dictionary ``kwargs`` or by using keyword arguments ``**init_kwargs``.
        These arguments are passed directly to WebDriver without any
        processing. See [https://seleniumhq.github.io/selenium/docs/api/py/api.html|
        Selenium API documentation] for details about the supported arguments.

        Examples:
        | # Use proxy with Firefox   |                |                              |                                      |
        | ${proxy}=                  | `Evaluate`     | selenium.webdriver.Proxy()   | modules=selenium, selenium.webdriver |
        | ${proxy.http_proxy}=       | `Set Variable` | localhost:8888               |                                      |
        | `Create Webdriver`         | Firefox        | proxy=${proxy}               |                                      |
        | # Use proxy with PhantomJS |                |                              |                                      |
        | ${service args}=           | `Create List`  | --proxy=192.168.132.104:8888 |                                      |
        | `Create Webdriver`         | PhantomJS      | service_args=${service args} |                                      |

        Returns the index of this browser instance which can be used later to
        switch back to it. Index starts from 1 and is reset back to it when
        `Close All Browsers` keyword is used. See `Switch Browser` for an
        example.
        """
        return self.browsermanagementkeywords.create_webdriver(driver_name, alias, kwargs, **init_kwargs)

    @keyword(name="Get Browser Aliases")
    def get_browser_aliases(self):
        """Returns aliases of all active browser that has an alias as NormalizedDict.
        The dictionary contains the aliases as keys and the index as value.
        This can be accessed as dictionary ``${aliases.key}`` or as list ``@{aliases}[0]``.

        Example:
        | `Open Browser` | https://example.com   | alias=BrowserA | |
        | `Open Browser` | https://example.com   | alias=BrowserB | |
        | &{aliases}     | `Get Browser Aliases` |                | # &{aliases} = { BrowserA=1|BrowserB=2 } |
        | `Log`          | ${aliases.BrowserA}   |                | # logs ``1`` |
        | FOR            | ${alias}              | IN             | @{aliases} |
        |                | `Log`                 | ${alias}       | # logs ``BrowserA`` and ``BrowserB`` |
        | END            |                       |                | |

        See `Switch Browser` for more information and examples.

        New in SeleniumLibrary 4.0
        """
        return self.browsermanagementkeywords.get_browser_aliases()

    @keyword(name="Get Browser Ids")
    def get_browser_ids(self):
        """Returns index of all active browser as list.

        Example:
        | @{browser_ids}= | Get Browser Ids   |                   |                |
        | FOR             | ${id}             | IN                | @{browser_ids} |
        |                 | @{window_titles}= | Get Window Titles | browser=${id}  |
        |                 | Log               | Browser ${id} has these windows: ${window_titles} | |
        | END             |                   |                   |                |

        See `Switch Browser` for more information and examples.

        New in SeleniumLibrary 4.0
        """
        return self.browsermanagementkeywords.get_browser_ids()

    @keyword(name="Get Location")
    def get_location(self):
        """Returns the current browser window URL."""
        return self.browsermanagementkeywords.get_location()

    @keyword(name="Get Selenium Implicit Wait")
    def get_selenium_implicit_wait(self):
        """Gets the implicit wait value used by Selenium.

        The value is returned as a human-readable string like ``1 second``.

        See the `Implicit wait` section above for more information.
        """
        return self.browsermanagementkeywords.get_selenium_implicit_wait()

    @keyword(name="Get Selenium Speed")
    def get_selenium_speed(self):
        """Gets the delay that is waited after each Selenium command.

        The value is returned as a human-readable string like ``1 second``.

        See the `Selenium Speed` section above for more information.
        """
        return self.browsermanagementkeywords.get_selenium_speed()

    @keyword(name="Get Selenium Timeout")
    def get_selenium_timeout(self):
        """Gets the timeout that is used by various keywords.

        The value is returned as a human-readable string like ``1 second``.

        See the `Timeout` section above for more information.
        """
        return self.browsermanagementkeywords.get_selenium_timeout()

    @keyword(name="Get Session Id")
    def get_session_id(self):
        """Returns the currently active browser session id.

        New in SeleniumLibrary 3.2
        """
        return self.browsermanagementkeywords.get_session_id()

    @keyword(name="Get Source")
    def get_source(self):
        """Returns the entire HTML source of the current page or frame."""
        return self.browsermanagementkeywords.get_source()

    @keyword(name="Get Title")
    def get_title(self):
        """Returns the title of the current page."""
        return self.browsermanagementkeywords.get_title()

    @keyword(name="Go Back")
    def go_back(self):
        """Simulates the user clicking the back button on their browser."""
        return self.browsermanagementkeywords.go_back()

    @keyword(name="Go To")
    def go_to(self, url):
        """Navigates the current browser window to the provided ``url``."""
        return self.browsermanagementkeywords.go_to(url)

    @keyword(name="Location Should Be")
    def location_should_be(self, url, message=None):
        """Verifies that the current URL is exactly ``url``.

        The ``url`` argument contains the exact url that should exist in browser.

        The ``message`` argument can be used to override the default error
        message.

        ``message`` argument is new in SeleniumLibrary 3.2.0.
        """
        return self.browsermanagementkeywords.location_should_be(url, message)

    @keyword(name="Location Should Contain")
    def location_should_contain(self, expected, message=None):
        """Verifies that the current URL contains ``expected``.

        The ``expected`` argument contains the expected value in url.

        The ``message`` argument can be used to override the default error
        message.

        ``message`` argument is new in SeleniumLibrary 3.2.0.
        """
        return self.browsermanagementkeywords.location_should_contain(expected, message)

    @keyword(name="Log Location")
    def log_location(self):
        """Logs and returns the current browser window URL."""
        return self.browsermanagementkeywords.log_location()

    @keyword(name="Log Source")
    def log_source(self, loglevel='INFO'):
        """Logs and returns the HTML source of the current page or frame.

        The ``loglevel`` argument defines the used log level. Valid log
        levels are ``WARN``, ``INFO`` (default), ``DEBUG``, ``TRACE``
        and ``NONE`` (no logging).
        """
        return self.browsermanagementkeywords.log_source(loglevel)

    @keyword(name="Log Title")
    def log_title(self):
        """Logs and returns the title of the current page."""
        return self.browsermanagementkeywords.log_title()

    @keyword(name="Open Browser")
    def open_browser(self, url=None, browser='firefox', alias=None, remote_url=False, desired_capabilities=None, ff_profile_dir=None, options=None, service_log_path=None, executable_path=None):
        """Opens a new browser instance to the optional ``url``.

        The ``browser`` argument specifies which browser to use. The
        supported browsers are listed in the table below. The browser names
        are case-insensitive and some browsers have multiple supported names.

        |    = Browser =    |        = Name(s) =       |
        | Firefox           | firefox, ff              |
        | Google Chrome     | googlechrome, chrome, gc |
        | Headless Firefox  | headlessfirefox          |
        | Headless Chrome   | headlesschrome           |
        | Internet Explorer | internetexplorer, ie     |
        | Edge              | edge                     |
        | Safari            | safari                   |
        | Opera             | opera                    |
        | Android           | android                  |
        | Iphone            | iphone                   |
        | PhantomJS         | phantomjs                |
        | HTMLUnit          | htmlunit                 |
        | HTMLUnit with Javascript | htmlunitwithjs    |

        To be able to actually use one of these browsers, you need to have
        a matching Selenium browser driver available. See the
        [https://github.com/robotframework/SeleniumLibrary#browser-drivers|
        project documentation] for more details. Headless Firefox and
        Headless Chrome are new additions in SeleniumLibrary 3.1.0
        and require Selenium 3.8.0 or newer.

        After opening the browser, it is possible to use optional
        ``url`` to navigate the browser to the desired address.

        Optional ``alias`` is an alias given for this browser instance and
        it can be used for switching between browsers. When same ``alias``
        is given with two `Open Browser` keywords, the first keyword will
        open a new browser, but the second one will switch to the already
        opened browser and will not open a new browser. The ``alias``
        definition overrules ``browser`` definition. When same ``alias``
        is used but a different ``browser`` is defined, then switch to
        a browser with same alias is done and new browser is not opened.
        An alternative approach for switching is using an index returned
        by this keyword. These indices start from 1, are incremented when new
        browsers are opened, and reset back to 1 when `Close All Browsers`
        is called. See `Switch Browser` for more information and examples.

        Optional ``remote_url`` is the URL for a
        [https://github.com/SeleniumHQ/selenium/wiki/Grid2|Selenium Grid].

        Optional ``desired_capabilities`` can be used to configure, for example,
        logging preferences for a browser or a browser and operating system
        when using [http://saucelabs.com|Sauce Labs]. Desired capabilities can
        be given either as a Python dictionary or as a string in the format
        ``key1:value1,key2:value2``.
        [https://github.com/SeleniumHQ/selenium/wiki/DesiredCapabilities|
        Selenium documentation] lists possible capabilities that can be
        enabled.

        Optional ``ff_profile_dir`` is the path to the Firefox profile
        directory if you wish to overwrite the default profile Selenium
        uses. Notice that prior to SeleniumLibrary 3.0, the library
        contained its own profile that was used by default. The
        ``ff_profile_dir`` can also be an instance of the
        [https://seleniumhq.github.io/selenium/docs/api/py/webdriver_firefox/selenium.webdriver.firefox.firefox_profile.html|selenium.webdriver.FirefoxProfile]
        . As a third option, it is possible to use `FirefoxProfile` methods
        and attributes to define the profile using methods and attributes
        in the same way as with ``options`` argument. Example: It is possible
        to use FirefoxProfile `set_preference` to define different
        profile settings. See ``options`` argument documentation in below
        how to handle backslash escaping.

        Optional ``options`` argument allows defining browser specific
        Selenium options. Example for Chrome, the ``options`` argument
        allows defining the following
        [https://seleniumhq.github.io/selenium/docs/api/py/webdriver_chrome/selenium.webdriver.chrome.options.html#selenium.webdriver.chrome.options.Options|methods and attributes]
        and for Firefox these
        [https://seleniumhq.github.io/selenium/docs/api/py/webdriver_firefox/selenium.webdriver.firefox.options.html?highlight=firefox#selenium.webdriver.firefox.options.Options|methods and attributes]
        are available. Please note that not all browsers, supported by the
        SeleniumLibrary, have Selenium options available. Therefore please
        consult the Selenium documentation which browsers do support
        the Selenium options. If ``browser`` argument is `android` then
        [https://seleniumhq.github.io/selenium/docs/api/py/webdriver_chrome/selenium.webdriver.chrome.options.html#selenium.webdriver.chrome.options.Options|Chrome options]
        is used. Selenium options are also supported, when ``remote_url``
        argument is used.

        The SeleniumLibrary ``options`` argument accepts Selenium
        options in two different formats: as a string and as Python object
        which is an instance of the Selenium options class.

        The string format allows defining Selenium options methods
        or attributes and their arguments in Robot Framework test data.
        The method and attributes names are case and space sensitive and
        must match to the Selenium options methods and attributes names.
        When defining a method, it must be defined in a similar way as in
        python: method name, opening parenthesis, zero to many arguments
        and closing parenthesis. If there is a need to define multiple
        arguments for a single method, arguments must be separated with
        comma, just like in Python. Example: `add_argument("--headless")`
        or `add_experimental_option("key", "value")`. Attributes are
        defined in a similar way as in Python: attribute name, equal sign,
        and attribute value. Example, `headless=True`. Multiple methods
        and attributes must be separated by a semicolon. Example:
        `add_argument("--headless");add_argument("--start-maximized")`.

        Arguments allow defining Python data types and arguments are
        evaluated by using Python
        [https://docs.python.org/3/library/ast.html#ast.literal_eval|ast.literal_eval].
        Strings must be quoted with single or double quotes, example "value"
        or 'value'. It is also possible to define other Python builtin
        data types, example `True` or `None`, by not using quotes
        around the arguments.

        The string format is space friendly. Usually, spaces do not alter
        the defining methods or attributes. There are two exceptions.
        In some Robot Framework test data formats, two or more spaces are
        considered as cell separator and instead of defining a single
        argument, two or more arguments may be defined. Spaces in string
        arguments are not removed and are left as is. Example
        `add_argument ( "--headless" )` is same as
        `add_argument("--headless")`. But `add_argument(" --headless ")` is
        not same same as `add_argument ( "--headless" )`, because
        spaces inside of quotes are not removed. Please note that if
        options string contains backslash, example a Windows OS path,
        the backslash needs escaping both in Robot Framework data and
        in Python side. This means single backslash must be writen using
        four backslash characters. Example, Windows path:
        "C:\path\to\profile" must be written as
        "C:\\\\path\\\to\\\\profile". Another way to write
        backslash is use Python
        [https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals|raw strings]
        and example write: r"C:\\path\\to\\profile".

        As last format, ``options`` argument also supports receiving
        the Selenium options as Python class instance. In this case, the
        instance is used as-is and the SeleniumLibrary will not convert
        the instance to other formats.
        For example, if the following code return value is saved to
        `${options}` variable in the Robot Framework data:
        | options = webdriver.ChromeOptions()
        | options.add_argument('--disable-dev-shm-usage')
        | return options

        Then the `${options}` variable can be used as an argument to
        ``options``.

        Example the ``options`` argument can be used to launch Chomium-based
        applications which utilize the
        [https://bitbucket.org/chromiumembedded/cef/wiki/UsingChromeDriver|Chromium Embedded Framework]
        . To lauch Chomium-based application, use ``options`` to define
        `binary_location` attribute and use `add_argument` method to define
        `remote-debugging-port` port for the application. Once the browser
        is opened, the test can interact with the embedded web-content of
        the system under test.

        Optional ``service_log_path`` argument defines the name of the
        file where to write the browser driver logs. If the
        ``service_log_path``  argument contain a  marker ``{index}``, it
        will be automatically replaced with unique running
        index preventing files to be overwritten. Indices start's from 1,
        and how they are represented can be customized using Python's
        [https://docs.python.org/3/library/string.html#format-string-syntax|
        format string syntax].

        Optional ``executable_path`` argument defines the path to the driver
        executable, example to a chromedriver or a geckodriver. If not defined
        it is assumed the executable is in the
        [https://en.wikipedia.org/wiki/PATH_(variable)|$PATH].

        Examples:
        | `Open Browser` | http://example.com | Chrome  |                                         |
        | `Open Browser` | http://example.com | Firefox | alias=Firefox                           |
        | `Open Browser` | http://example.com | Edge    | remote_url=http://127.0.0.1:4444/wd/hub |
        | `Open Browser` | about:blank        |         |                                         |
        | `Open Browser` | browser=Chrome     |         |                                         |

        Alias examples:
        | ${1_index} =    | `Open Browser` | http://example.com | Chrome  | alias=Chrome     | # Opens new browser because alias is new.         |
        | ${2_index} =    | `Open Browser` | http://example.com | Firefox |                  | # Opens new browser because alias is not defined. |
        | ${3_index} =    | `Open Browser` | http://example.com | Chrome  | alias=Chrome     | # Switches to the browser with Chrome alias.      |
        | ${4_index} =    | `Open Browser` | http://example.com | Chrome  | alias=${1_index} | # Switches to the browser with Chrome alias.      |
        | Should Be Equal | ${1_index}     | ${3_index}         |         |                  |                                                   |
        | Should Be Equal | ${1_index}     | ${4_index}         |         |                  |                                                   |
        | Should Be Equal | ${2_index}     | ${2}               |         |                  |                                                   |

        Example when using
        [https://seleniumhq.github.io/selenium/docs/api/py/webdriver_chrome/selenium.webdriver.chrome.options.html#selenium.webdriver.chrome.options.Options|Chrome options]
        method:
        | `Open Browser` | http://example.com | Chrome | options=add_argument("--disable-popup-blocking"); add_argument("--ignore-certificate-errors") | # Sting format.                    |
        |  ${options} =  |     Get Options    |        |                                                                                               | # Selenium options instance.       |
        | `Open Browser` | http://example.com | Chrome | options=${options}                                                                            |                                    |
        | `Open Browser` | None               | Chrome | options=binary_location="/path/to/binary";add_argument("remote-debugging-port=port")          | # Start Chomium-based application. |
        | `Open Browser` | None               | Chrome | options=binary_location=r"C:\\path\\to\\binary"                                         | # Windows OS path escaping.        |

        Example for FirefoxProfile
        | `Open Browser` | http://example.com | Firefox | ff_profile_dir=/path/to/profile                                                  | # Using profile from disk.                       |
        | `Open Browser` | http://example.com | Firefox | ff_profile_dir=${FirefoxProfile_instance}                                        | # Using instance of FirefoxProfile.              |
        | `Open Browser` | http://example.com | Firefox | ff_profile_dir=set_preference("key", "value");set_preference("other", "setting") | # Defining profile using FirefoxProfile mehtods. |

        If the provided configuration options are not enough, it is possible
        to use `Create Webdriver` to customize browser initialization even
        more.

        Applying ``desired_capabilities`` argument also for local browser is
        new in SeleniumLibrary 3.1.

        Using ``alias`` to decide, is the new browser opened is new
        in SeleniumLibrary 4.0. The ``options`` and ``service_log_path``
        are new in SeleniumLibrary 4.0. Support for ``ff_profile_dir``
        accepting an instance of the `selenium.webdriver.FirefoxProfile`
        and support defining FirefoxProfile with methods and
        attributes are new in SeleniumLibrary 4.0.

        Making ``url`` optional is new in SeleniumLibrary 4.1.

        The ``executable_path`` argument is new in SeleniumLibrary 4.2.
        """
        return self.browsermanagementkeywords.open_browser(url, browser, alias, remote_url, desired_capabilities, ff_profile_dir, options, service_log_path, executable_path)

    @keyword(name="Reload Page")
    def reload_page(self):
        """Simulates user reloading page."""
        return self.browsermanagementkeywords.reload_page()

    @keyword(name="Set Browser Implicit Wait")
    def set_browser_implicit_wait(self, value):
        """Sets the implicit wait value used by Selenium.

        Same as `Set Selenium Implicit Wait` but only affects the current
        browser.
        """
        return self.browsermanagementkeywords.set_browser_implicit_wait(value)

    @keyword(name="Set Selenium Implicit Wait")
    def set_selenium_implicit_wait(self, value):
        """Sets the implicit wait value used by Selenium.

        The value can be given as a number that is considered to be
        seconds or as a human-readable string like ``1 second``.
        The previous value is returned and can be used to restore
        the original value later if needed.

        This keyword sets the implicit wait for all opened browsers.
        Use `Set Browser Implicit Wait` to set it only to the current
        browser.

        See the `Implicit wait` section above for more information.

        Example:
        | ${orig wait} = | `Set Selenium Implicit Wait` | 10 seconds |
        | `Perform AJAX call that is slow` |
        | `Set Selenium Implicit Wait` | ${orig wait} |
        """
        return self.browsermanagementkeywords.set_selenium_implicit_wait(value)

    @keyword(name="Set Selenium Speed")
    def set_selenium_speed(self, value):
        """Sets the delay that is waited after each Selenium command.

        The value can be given as a number that is considered to be
        seconds or as a human-readable string like ``1 second``.
        The previous value is returned and can be used to restore
        the original value later if needed.

        See the `Selenium Speed` section above for more information.

        Example:
        | `Set Selenium Speed` | 0.5 seconds |
        """
        return self.browsermanagementkeywords.set_selenium_speed(value)

    @keyword(name="Set Selenium Timeout")
    def set_selenium_timeout(self, value):
        """Sets the timeout that is used by various keywords.

        The value can be given as a number that is considered to be
        seconds or as a human-readable string like ``1 second``.
        The previous value is returned and can be used to restore
        the original value later if needed.

        See the `Timeout` section above for more information.

        Example:
        | ${orig timeout} = | `Set Selenium Timeout` | 15 seconds |
        | `Open page that loads slowly` |
        | `Set Selenium Timeout` | ${orig timeout} |
        """
        return self.browsermanagementkeywords.set_selenium_timeout(value)

    @keyword(name="Switch Browser")
    def switch_browser(self, index_or_alias):
        """Switches between active browsers using ``index_or_alias``.

        Indices are returned by the `Open Browser` keyword and aliases can
        be given to it explicitly. Indices start from 1.

        Example:
        | `Open Browser`        | http://google.com | ff       |
        | `Location Should Be`  | http://google.com |          |
        | `Open Browser`        | http://yahoo.com  | ie       | alias=second |
        | `Location Should Be`  | http://yahoo.com  |          |
        | `Switch Browser`      | 1                 | # index  |
        | `Page Should Contain` | I'm feeling lucky |          |
        | `Switch Browser`      | second            | # alias  |
        | `Page Should Contain` | More Yahoo!       |          |
        | `Close All Browsers`  |                   |          |

        Above example expects that there was no other open browsers when
        opening the first one because it used index ``1`` when switching to
        it later. If you are not sure about that, you can store the index
        into a variable as below.

        | ${index} =         | `Open Browser` | http://google.com |
        | # Do something ... |                |                   |
        | `Switch Browser`   | ${index}       |                   |
        """
        return self.browsermanagementkeywords.switch_browser(index_or_alias)

    @keyword(name="Title Should Be")
    def title_should_be(self, title, message=None):
        """Verifies that the current page title equals ``title``.

        The ``message`` argument can be used to override the default error
        message.

        ``message`` argument is new in SeleniumLibrary 3.1.
        """
        return self.browsermanagementkeywords.title_should_be(title, message)

    @keyword(name="Add Cookie")
    def add_cookie(self, name, value, path=None, domain=None, secure=None, expiry=None):
        """Adds a cookie to your current session.

        ``name`` and ``value`` are required, ``path``, ``domain``, ``secure``
        and ``expiry`` are optional.  Expiry supports the same formats as
        the [http://robotframework.org/robotframework/latest/libraries/DateTime.html|DateTime]
        library or an epoch timestamp.

        Example:
        | `Add Cookie` | foo | bar |                            |
        | `Add Cookie` | foo | bar | domain=example.com         |
        | `Add Cookie` | foo | bar | expiry=2027-09-28 16:21:35 | # Expiry as timestamp.     |
        | `Add Cookie` | foo | bar | expiry=1822137695          | # Expiry as epoch seconds. |

        Prior to SeleniumLibrary 3.0 setting expiry did not work.
        """
        return self.cookiekeywords.add_cookie(name, value, path, domain, secure, expiry)

    @keyword(name="Delete All Cookies")
    def delete_all_cookies(self):
        """Deletes all cookies."""
        return self.cookiekeywords.delete_all_cookies()

    @keyword(name="Delete Cookie")
    def delete_cookie(self, name):
        """Deletes the cookie matching ``name``.

        If the cookie is not found, nothing happens.
        """
        return self.cookiekeywords.delete_cookie(name)

    @keyword(name="Get Cookie")
    def get_cookie(self, name):
        """Returns information of cookie with ``name`` as an object.

        If no cookie is found with ``name``, keyword fails. The cookie object
        contains details about the cookie. Attributes available in the object
        are documented in the table below.

        | = Attribute = |             = Explanation =                                |
        | name          | The name of a cookie.                                      |
        | value         | Value of the cookie.                                       |
        | path          | Indicates a URL path, for example ``/``.                   |
        | domain        | The domain, the cookie is visible to.                      |
        | secure        | When true, the cookie is only used with HTTPS connections. |
        | httpOnly      | When true, the cookie is not accessible via JavaScript.    |
        | expiry        | Python datetime object indicating when the cookie expires. |
        | extra         | Possible attributes outside of the WebDriver specification |

        See the
        [https://w3c.github.io/webdriver/#cookies|WebDriver specification]
        for details about the cookie information.
        Notice that ``expiry`` is specified as a
        [https://docs.python.org/3/library/datetime.html#datetime.datetime|datetime object],
        not as seconds since Unix Epoch like WebDriver natively does.

        In some cases, example when running a browser in the cloud, it is possible that
        the cookie contains other attributes than is defined in the
        [https://w3c.github.io/webdriver/#cookies|WebDriver specification].
        These other attributes are available in an ``extra`` attribute in the cookie
        object and it contains a dictionary of the other attributes. The ``extra``
        attribute is new in SeleniumLibrary 4.0.

        Example:
        | `Add Cookie`      | foo             | bar |
        | ${cookie} =       | `Get Cookie`    | foo |
        | `Should Be Equal` | ${cookie.name}  | bar |
        | `Should Be Equal` | ${cookie.value} | foo |
        | `Should Be True`  | ${cookie.expiry.year} > 2017 |

        New in SeleniumLibrary 3.0.
        """
        return self.cookiekeywords.get_cookie(name)

    @keyword(name="Get Cookies")
    def get_cookies(self, as_dict=False):
        """Returns all cookies of the current page.

        If ``as_dict`` argument evaluates as false, see `Boolean arguments`
        for more details, then cookie information is returned as
        a single string in format ``name1=value1; name2=value2; name3=value3``.
        When ``as_dict`` argument evaluates as true, cookie information
        is returned as Robot Framework dictionary format. The string format
        can be used, for example, for logging purposes or in headers when
        sending HTTP requests. The dictionary format is helpful when
        the result can be passed to requests library's Create Session
        keyword's optional cookies parameter.

        The `` as_dict`` argument is new in SeleniumLibrary 3.3
        """
        return self.cookiekeywords.get_cookies(as_dict)

    @keyword(name="Add Location Strategy")
    def add_location_strategy(self, strategy_name, strategy_keyword, persist=False):
        """Adds a custom location strategy.

        See `Custom locators` for information on how to create and use
        custom strategies. `Remove Location Strategy` can be used to
        remove a registered strategy.

        Location strategies are automatically removed after leaving the
        current scope by default. Setting ``persist`` to a true value (see
        `Boolean arguments`) will cause the location strategy to stay
        registered throughout the life of the test.
        """
        return self.elementkeywords.add_location_strategy(strategy_name, strategy_keyword, persist)

    @keyword(name="Assign Id To Element")
    def assign_id_to_element(self, locator, id):
        """Assigns a temporary ``id`` to the element specified by ``locator``.

        This is mainly useful if the locator is complicated and/or slow XPath
        expression and it is needed multiple times. Identifier expires when
        the page is reloaded.

        See the `Locating elements` section for details about the locator
        syntax.

        Example:
        | `Assign ID to Element` | //ul[@class='example' and ./li[contains(., 'Stuff')]] | my id |
        | `Page Should Contain Element` | my id |
        """
        return self.elementkeywords.assign_id_to_element(locator, id)

    @keyword(name="Clear Element Text")
    def clear_element_text(self, locator):
        """Clears the value of the text-input-element identified by ``locator``.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.elementkeywords.clear_element_text(locator)

    @keyword(name="Click Button")
    def click_button(self, locator, modifier=False):
        """Clicks the button identified by ``locator``.

        See the `Locating elements` section for details about the locator
        syntax. When using the default locator strategy, buttons are
        searched using ``id``, ``name``, and ``value``.

        See the `Click Element` keyword for details about the
        ``modifier`` argument.

        The ``modifier`` argument is new in SeleniumLibrary 3.3
        """
        return self.elementkeywords.click_button(locator, modifier)

    @keyword(name="Click Element")
    def click_element(self, locator, modifier=False, action_chain=False):
        """Click the element identified by ``locator``.

        See the `Locating elements` section for details about the locator
        syntax.

        The ``modifier`` argument can be used to pass
        [https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.keys.html#selenium.webdriver.common.keys.Keys|Selenium Keys]
        when clicking the element. The `+` can be used as a separator
        for different Selenium Keys. The `CTRL` is internally translated to
        the `CONTROL` key. The ``modifier`` is space and case insensitive, example
        "alt" and " aLt " are supported formats to
        [https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.keys.html#selenium.webdriver.common.keys.Keys.ALT|ALT key]
        . If ``modifier`` does not match to Selenium Keys, keyword fails.

        If ``action_chain`` argument is true, see `Boolean arguments` for more
        details on how to set boolean argument, then keyword uses ActionChain
        based click instead of the <web_element>.click() function. If both
        ``action_chain`` and ``modifier`` are defined, the click will be
        performed using ``modifier`` and ``action_chain`` will be ignored.

        Example:
        | Click Element | id:button |                   | # Would click element without any modifiers.               |
        | Click Element | id:button | CTRL              | # Would click element with CTLR key pressed down.          |
        | Click Element | id:button | CTRL+ALT          | # Would click element with CTLR and ALT keys pressed down. |
        | Click Element | id:button | action_chain=True | # Clicks the button using an Selenium  ActionChains        |

        The ``modifier`` argument is new in SeleniumLibrary 3.2
        The ``action_chain`` argument is new in SeleniumLibrary 4.1
        """
        return self.elementkeywords.click_element(locator, modifier, action_chain)

    @keyword(name="Click Element At Coordinates")
    def click_element_at_coordinates(self, locator, xoffset, yoffset):
        """Click the element ``locator`` at ``xoffset/yoffset``.

        The Cursor is moved and the center of the element and x/y coordinates are
        calculated from that point.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.elementkeywords.click_element_at_coordinates(locator, xoffset, yoffset)

    @keyword(name="Click Image")
    def click_image(self, locator, modifier=False):
        """Clicks an image identified by ``locator``.

        See the `Locating elements` section for details about the locator
        syntax. When using the default locator strategy, images are searched
        using ``id``, ``name``, ``src`` and ``alt``.

        See the `Click Element` keyword for details about the
        ``modifier`` argument.

        The ``modifier`` argument is new in SeleniumLibrary 3.3
        """
        return self.elementkeywords.click_image(locator, modifier)

    @keyword(name="Click Link")
    def click_link(self, locator, modifier=False):
        """Clicks a link identified by ``locator``.

        See the `Locating elements` section for details about the locator
        syntax. When using the default locator strategy, links are searched
        using ``id``, ``name``, ``href`` and the link text.

        See the `Click Element` keyword for details about the
        ``modifier`` argument.

        The ``modifier`` argument is new in SeleniumLibrary 3.3
        """
        return self.elementkeywords.click_link(locator, modifier)

    @keyword(name="Cover Element")
    def cover_element(self, locator):
        """Will cover elements identified by ``locator`` with a blue div without breaking page layout.

        See the `Locating elements` section for details about the locator
        syntax.

        New in SeleniumLibrary 3.3.0

        Example:
        |`Cover Element` | css:div#container |
        """
        return self.elementkeywords.cover_element(locator)

    @keyword(name="Double Click Element")
    def double_click_element(self, locator):
        """Double clicks the element identified by ``locator``.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.elementkeywords.double_click_element(locator)

    @keyword(name="Drag And Drop")
    def drag_and_drop(self, locator, target):
        """Drags the element identified by ``locator`` into the ``target`` element.

        The ``locator`` argument is the locator of the dragged element
        and the ``target`` is the locator of the target. See the
        `Locating elements` section for details about the locator syntax.

        Example:
        | `Drag And Drop` | css:div#element | css:div.target |
        """
        return self.elementkeywords.drag_and_drop(locator, target)

    @keyword(name="Drag And Drop By Offset")
    def drag_and_drop_by_offset(self, locator, xoffset, yoffset):
        """Drags the element identified with ``locator`` by ``xoffset/yoffset``.

        See the `Locating elements` section for details about the locator
        syntax.

        The element will be moved by ``xoffset`` and ``yoffset``, each of which
        is a negative or positive number specifying the offset.

        Example:
        | `Drag And Drop By Offset` | myElem | 50 | -35 | # Move myElem 50px right and 35px down |
        """
        return self.elementkeywords.drag_and_drop_by_offset(locator, xoffset, yoffset)

    @keyword(name="Element Attribute Value Should Be")
    def element_attribute_value_should_be(self, locator, attribute, expected, message=None):
        """Verifies element identified by ``locator`` contains expected attribute value.

        See the `Locating elements` section for details about the locator
        syntax.

        Example:
        `Element Attribute Value Should Be` | css:img | href | value

        New in SeleniumLibrary 3.2.
        """
        return self.elementkeywords.element_attribute_value_should_be(locator, attribute, expected, message)

    @keyword(name="Element Should Be Disabled")
    def element_should_be_disabled(self, locator):
        """Verifies that element identified by ``locator`` is disabled.

        This keyword considers also elements that are read-only to be
        disabled.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.elementkeywords.element_should_be_disabled(locator)

    @keyword(name="Element Should Be Enabled")
    def element_should_be_enabled(self, locator):
        """Verifies that element identified by ``locator`` is enabled.

        This keyword considers also elements that are read-only to be
        disabled.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.elementkeywords.element_should_be_enabled(locator)

    @keyword(name="Element Should Be Focused")
    def element_should_be_focused(self, locator):
        """Verifies that element identified by ``locator`` is focused.

        See the `Locating elements` section for details about the locator
        syntax.

        New in SeleniumLibrary 3.0.
        """
        return self.elementkeywords.element_should_be_focused(locator)

    @keyword(name="Element Should Be Visible")
    def element_should_be_visible(self, locator, message=None):
        """Verifies that the element identified by ``locator`` is visible.

        Herein, visible means that the element is logically visible, not
        optically visible in the current browser viewport. For example,
        an element that carries ``display:none`` is not logically visible,
        so using this keyword on that element would fail.

        See the `Locating elements` section for details about the locator
        syntax.

        The ``message`` argument can be used to override the default error
        message.
        """
        return self.elementkeywords.element_should_be_visible(locator, message)

    @keyword(name="Element Should Contain")
    def element_should_contain(self, locator, expected, message=None, ignore_case=False):
        """Verifies that element ``locator`` contains text ``expected``.

        See the `Locating elements` section for details about the locator
        syntax.

        The ``message`` argument can be used to override the default error
        message.

        The ``ignore_case`` argument can be set to True to compare case
        insensitive, default is False. New in SeleniumLibrary 3.1.

        ``ignore_case`` argument is new in SeleniumLibrary 3.1.

        Use `Element Text Should Be` if you want to match the exact text,
        not a substring.
        """
        return self.elementkeywords.element_should_contain(locator, expected, message, ignore_case)

    @keyword(name="Element Should Not Be Visible")
    def element_should_not_be_visible(self, locator, message=None):
        """Verifies that the element identified by ``locator`` is NOT visible.

        Passes if the element does not exists. See `Element Should Be Visible`
        for more information about visibility and supported arguments.
        """
        return self.elementkeywords.element_should_not_be_visible(locator, message)

    @keyword(name="Element Should Not Contain")
    def element_should_not_contain(self, locator, expected, message=None, ignore_case=False):
        """Verifies that element ``locator`` does not contain text ``expected``.

        See the `Locating elements` section for details about the locator
        syntax.

        The ``message`` argument can be used to override the default error
        message.

        The ``ignore_case`` argument can be set to True to compare case
        insensitive, default is False.

        ``ignore_case`` argument new in SeleniumLibrary 3.1.
        """
        return self.elementkeywords.element_should_not_contain(locator, expected, message, ignore_case)

    @keyword(name="Element Text Should Be")
    def element_text_should_be(self, locator, expected, message=None, ignore_case=False):
        """Verifies that element ``locator`` contains exact the text ``expected``.

        See the `Locating elements` section for details about the locator
        syntax.

        The ``message`` argument can be used to override the default error
        message.

        The ``ignore_case`` argument can be set to True to compare case
        insensitive, default is False.

        ``ignore_case`` argument is new in SeleniumLibrary 3.1.

        Use `Element Should Contain` if a substring match is desired.
        """
        return self.elementkeywords.element_text_should_be(locator, expected, message, ignore_case)

    @keyword(name="Element Text Should Not Be")
    def element_text_should_not_be(self, locator, not_expected, message=None, ignore_case=False):
        """Verifies that element ``locator`` does not contain exact the text ``not_expected``.

        See the `Locating elements` section for details about the locator
        syntax.

        The ``message`` argument can be used to override the default error
        message.

        The ``ignore_case`` argument can be set to True to compare case
        insensitive, default is False.

        New in SeleniumLibrary 3.1.1
        """
        return self.elementkeywords.element_text_should_not_be(locator, not_expected, message, ignore_case)

    @keyword(name="Get All Links")
    def get_all_links(self):
        """Returns a list containing ids of all links found in current page.

        If a link has no id, an empty string will be in the list instead.
        """
        return self.elementkeywords.get_all_links()

    @keyword(name="Get Element Attribute")
    def get_element_attribute(self, locator, attribute):
        """Returns the value of ``attribute`` from the element ``locator``.

        See the `Locating elements` section for details about the locator
        syntax.

        Example:
        | ${id}= | `Get Element Attribute` | css:h1 | id |

        Passing attribute name as part of the ``locator`` was removed
        in SeleniumLibrary 3.2. The explicit ``attribute`` argument
        should be used instead.
        """
        return self.elementkeywords.get_element_attribute(locator, attribute)

    @keyword(name="Get Element Count")
    def get_element_count(self, locator):
        """Returns the number of elements matching ``locator``.

        If you wish to assert the number of matching elements, use
        `Page Should Contain Element` with ``limit`` argument. Keyword will
        always return an integer.

        Example:
        | ${count} =       | `Get Element Count` | name:div_name  |
        | `Should Be True` | ${count} > 2        |                |

        New in SeleniumLibrary 3.0.
        """
        return self.elementkeywords.get_element_count(locator)

    @keyword(name="Get Element Size")
    def get_element_size(self, locator):
        """Returns width and height of the element identified by ``locator``.

        See the `Locating elements` section for details about the locator
        syntax.

        Both width and height are returned as integers.

        Example:
        | ${width} | ${height} = | `Get Element Size` | css:div#container |
        """
        return self.elementkeywords.get_element_size(locator)

    @keyword(name="Get Horizontal Position")
    def get_horizontal_position(self, locator):
        """Returns the horizontal position of the element identified by ``locator``.

        See the `Locating elements` section for details about the locator
        syntax.

        The position is returned in pixels off the left side of the page,
        as an integer.

        See also `Get Vertical Position`.
        """
        return self.elementkeywords.get_horizontal_position(locator)

    @keyword(name="Get Text")
    def get_text(self, locator):
        """Returns the text value of the element identified by ``locator``.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.elementkeywords.get_text(locator)

    @keyword(name="Get Value")
    def get_value(self, locator):
        """Returns the value attribute of the element identified by ``locator``.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.elementkeywords.get_value(locator)

    @keyword(name="Get Vertical Position")
    def get_vertical_position(self, locator):
        """Returns the vertical position of the element identified by ``locator``.

        See the `Locating elements` section for details about the locator
        syntax.

        The position is returned in pixels off the top of the page,
        as an integer.

        See also `Get Horizontal Position`.
        """
        return self.elementkeywords.get_vertical_position(locator)

    @keyword(name="Get Webelement")
    def get_webelement(self, locator):
        """Returns the first WebElement matching the given ``locator``.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.elementkeywords.get_webelement(locator)

    @keyword(name="Get Webelements")
    def get_webelements(self, locator):
        """Returns a list of WebElement objects matching the ``locator``.

        See the `Locating elements` section for details about the locator
        syntax.

        Starting from SeleniumLibrary 3.0, the keyword returns an empty
        list if there are no matching elements. In previous releases, the
        keyword failed in this case.
        """
        return self.elementkeywords.get_webelements(locator)

    @keyword(name="Locator Should Match X Times")
    def locator_should_match_x_times(self, locator, x, message=None, loglevel='TRACE'):
        """*DEPRECATED in SeleniumLibrary 4.0.*, use `Page Should Contain Element` with ``limit`` argument instead."""
        return self.elementkeywords.locator_should_match_x_times(locator, x, message, loglevel)

    @keyword(name="Mouse Down")
    def mouse_down(self, locator):
        """Simulates pressing the left mouse button on the element ``locator``.

        See the `Locating elements` section for details about the locator
        syntax.

        The element is pressed without releasing the mouse button.

        See also the more specific keywords `Mouse Down On Image` and
        `Mouse Down On Link`.
        """
        return self.elementkeywords.mouse_down(locator)

    @keyword(name="Mouse Down On Image")
    def mouse_down_on_image(self, locator):
        """Simulates a mouse down event on an image identified by ``locator``.

        See the `Locating elements` section for details about the locator
        syntax. When using the default locator strategy, images are searched
        using ``id``, ``name``, ``src`` and ``alt``.
        """
        return self.elementkeywords.mouse_down_on_image(locator)

    @keyword(name="Mouse Down On Link")
    def mouse_down_on_link(self, locator):
        """Simulates a mouse down event on a link identified by ``locator``.

        See the `Locating elements` section for details about the locator
        syntax. When using the default locator strategy, links are searched
        using ``id``, ``name``, ``href`` and the link text.
        """
        return self.elementkeywords.mouse_down_on_link(locator)

    @keyword(name="Mouse Out")
    def mouse_out(self, locator):
        """Simulates moving the mouse away from the element ``locator``.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.elementkeywords.mouse_out(locator)

    @keyword(name="Mouse Over")
    def mouse_over(self, locator):
        """Simulates hovering the mouse over the element ``locator``.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.elementkeywords.mouse_over(locator)

    @keyword(name="Mouse Up")
    def mouse_up(self, locator):
        """Simulates releasing the left mouse button on the element ``locator``.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.elementkeywords.mouse_up(locator)

    @keyword(name="Open Context Menu")
    def open_context_menu(self, locator):
        """Opens the context menu on the element identified by ``locator``."""
        return self.elementkeywords.open_context_menu(locator)

    @keyword(name="Page Should Contain")
    def page_should_contain(self, text, loglevel='TRACE'):
        """Verifies that current page contains ``text``.

        If this keyword fails, it automatically logs the page source
        using the log level specified with the optional ``loglevel``
        argument. Valid log levels are ``DEBUG``, ``INFO`` (default),
        ``WARN``, and ``NONE``. If the log level is ``NONE`` or below
        the current active log level the source will not be logged.
        """
        return self.elementkeywords.page_should_contain(text, loglevel)

    @keyword(name="Page Should Contain Element")
    def page_should_contain_element(self, locator, message=None, loglevel='TRACE', limit=None):
        """Verifies that element ``locator`` is found on the current page.

        See the `Locating elements` section for details about the locator
        syntax.

        The ``message`` argument can be used to override the default error
        message.

        The ``limit`` argument can used to define how many elements the
        page should contain. When ``limit`` is ``None`` (default) page can
        contain one or more elements. When limit is a number, page must
        contain same number of elements.

        See `Page Should Contain` for an explanation about the ``loglevel``
        argument.

        Examples assumes that locator matches to two elements.
        | `Page Should Contain Element` | div_name | limit=1    | # Keyword fails.                  |
        | `Page Should Contain Element` | div_name | limit=2    | # Keyword passes.                 |
        | `Page Should Contain Element` | div_name | limit=none | # None is considered one or more. |
        | `Page Should Contain Element` | div_name |            | # Same as above.                  |

        The ``limit`` argument is new in SeleniumLibrary 3.0.
        """
        return self.elementkeywords.page_should_contain_element(locator, message, loglevel, limit)

    @keyword(name="Page Should Contain Image")
    def page_should_contain_image(self, locator, message=None, loglevel='TRACE'):
        """Verifies image identified by ``locator`` is found from current page.

        See the `Locating elements` section for details about the locator
        syntax. When using the default locator strategy, images are searched
        using ``id``, ``name``, ``src`` and ``alt``.

        See `Page Should Contain Element` for an explanation about ``message``
        and ``loglevel`` arguments.
        """
        return self.elementkeywords.page_should_contain_image(locator, message, loglevel)

    @keyword(name="Page Should Contain Link")
    def page_should_contain_link(self, locator, message=None, loglevel='TRACE'):
        """Verifies link identified by ``locator`` is found from current page.

        See the `Locating elements` section for details about the locator
        syntax. When using the default locator strategy, links are searched
        using ``id``, ``name``, ``href`` and the link text.

        See `Page Should Contain Element` for an explanation about ``message``
        and ``loglevel`` arguments.
        """
        return self.elementkeywords.page_should_contain_link(locator, message, loglevel)

    @keyword(name="Page Should Not Contain")
    def page_should_not_contain(self, text, loglevel='TRACE'):
        """Verifies the current page does not contain ``text``.

        See `Page Should Contain` for an explanation about the ``loglevel``
        argument.
        """
        return self.elementkeywords.page_should_not_contain(text, loglevel)

    @keyword(name="Page Should Not Contain Element")
    def page_should_not_contain_element(self, locator, message=None, loglevel='TRACE'):
        """Verifies that element ``locator`` is found on the current page.

        See the `Locating elements` section for details about the locator
        syntax.

        See `Page Should Contain` for an explanation about ``message`` and
        ``loglevel`` arguments.
        """
        return self.elementkeywords.page_should_not_contain_element(locator, message, loglevel)

    @keyword(name="Page Should Not Contain Image")
    def page_should_not_contain_image(self, locator, message=None, loglevel='TRACE'):
        """Verifies image identified by ``locator`` is found from current page.

        See the `Locating elements` section for details about the locator
        syntax. When using the default locator strategy, images are searched
        using ``id``, ``name``, ``src`` and ``alt``.

        See `Page Should Contain Element` for an explanation about ``message``
        and ``loglevel`` arguments.
        """
        return self.elementkeywords.page_should_not_contain_image(locator, message, loglevel)

    @keyword(name="Page Should Not Contain Link")
    def page_should_not_contain_link(self, locator, message=None, loglevel='TRACE'):
        """Verifies link identified by ``locator`` is not found from current page.

        See the `Locating elements` section for details about the locator
        syntax. When using the default locator strategy, links are searched
        using ``id``, ``name``, ``href`` and the link text.

        See `Page Should Contain Element` for an explanation about ``message``
        and ``loglevel`` arguments.
        """
        return self.elementkeywords.page_should_not_contain_link(locator, message, loglevel)

    @keyword(name="Press Key")
    def press_key(self, locator, key):
        """*DEPRECATED in SeleniumLibrary 4.0.* use `Press Keys` instead."""
        return self.elementkeywords.press_key(locator, key)

    @keyword(name="Press Keys")
    def press_keys(self, locator=None, *keys):
        """Simulates the user pressing key(s) to an element or on the active browser.

        If ``locator`` evaluates as false, see `Boolean arguments` for more
        details, then the ``keys`` are sent to the currently active browser.
        Otherwise element is searched and ``keys`` are send to the element
        identified by the ``locator``. In later case, keyword fails if element
        is not found. See the `Locating elements` section for details about
        the locator syntax.

        ``keys`` arguments can contain one or many strings, but it can not
        be empty. ``keys`` can also be a combination of
        [https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.keys.html|Selenium Keys]
        and strings or a single Selenium Key. If Selenium Key is combined
        with strings, Selenium key and strings must be separated by the
        `+` character, like in `CONTROL+c`. Selenium Keys
        are space and case sensitive and Selenium Keys are not parsed
        inside of the string. Example AALTO, would send string `AALTO`
        and `ALT` not parsed inside of the string. But `A+ALT+O` would
        found Selenium ALT key from the ``keys`` argument. It also possible
        to press many Selenium Keys down at the same time, example
        'ALT+ARROW_DOWN`.

        If Selenium Keys are detected in the ``keys`` argument, keyword
        will press the Selenium Key down, send the strings and
         then release the Selenium Key. If keyword needs to send a Selenium
        Key as a string, then each character must be separated with
        `+` character, example `E+N+D`.

        `CTRL` is alias for
        [https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.keys.html#selenium.webdriver.common.keys.Keys.CONTROL|Selenium CONTROL]
        and ESC is alias for
        [https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.keys.html#selenium.webdriver.common.keys.Keys.ESCAPE|Selenium ESCAPE]

        New in SeleniumLibrary 3.3

        Examples:
        | `Press Keys` | text_field | AAAAA          |            | # Sends string "AAAAA" to element.                                                |
        | `Press Keys` | None       | BBBBB          |            | # Sends string "BBBBB" to currently active browser.                               |
        | `Press Keys` | text_field | E+N+D          |            | # Sends string "END" to element.                                                  |
        | `Press Keys` | text_field | XXX            | YY         | # Sends strings "XXX" and "YY" to element.                                        |
        | `Press Keys` | text_field | XXX+YY         |            | # Same as above.                                                                  |
        | `Press Keys` | text_field | ALT+ARROW_DOWN |            | # Pressing "ALT" key down, then pressing ARROW_DOWN and then releasing both keys. |
        | `Press Keys` | text_field | ALT            | ARROW_DOWN | # Pressing "ALT" key and then pressing ARROW_DOWN.                                |
        | `Press Keys` | text_field | CTRL+c         |            | # Pressing CTRL key down, sends string "c" and then releases CTRL key.            |
        | `Press Keys` | button     | RETURN         |            | # Pressing "ENTER" key to element.                                                |
        """
        return self.elementkeywords.press_keys(locator, *keys)

    @keyword(name="Remove Location Strategy")
    def remove_location_strategy(self, strategy_name):
        """Removes a previously added custom location strategy.

        See `Custom locators` for information on how to create and use
        custom strategies.
        """
        return self.elementkeywords.remove_location_strategy(strategy_name)

    @keyword(name="Scroll Element Into View")
    def scroll_element_into_view(self, locator):
        """Scrolls the element identified by ``locator`` into view.

        See the `Locating elements` section for details about the locator
        syntax.

        New in SeleniumLibrary 3.2.0
        """
        return self.elementkeywords.scroll_element_into_view(locator)

    @keyword(name="Set Focus To Element")
    def set_focus_to_element(self, locator):
        """Sets the focus to the element identified by ``locator``.

        See the `Locating elements` section for details about the locator
        syntax.

        Prior to SeleniumLibrary 3.0 this keyword was named `Focus`.
        """
        return self.elementkeywords.set_focus_to_element(locator)

    @keyword(name="Simulate Event")
    def simulate_event(self, locator, event):
        """Simulates ``event`` on the element identified by ``locator``.

        This keyword is useful if element has ``OnEvent`` handler that
        needs to be explicitly invoked.

        See the `Locating elements` section for details about the locator
        syntax.

        Prior to SeleniumLibrary 3.0 this keyword was named `Simulate`.
        """
        return self.elementkeywords.simulate_event(locator, event)

    @keyword(name="Checkbox Should Be Selected")
    def checkbox_should_be_selected(self, locator):
        """Verifies checkbox ``locator`` is selected/checked.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.formelementkeywords.checkbox_should_be_selected(locator)

    @keyword(name="Checkbox Should Not Be Selected")
    def checkbox_should_not_be_selected(self, locator):
        """Verifies checkbox ``locator`` is not selected/checked.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.formelementkeywords.checkbox_should_not_be_selected(locator)

    @keyword(name="Choose File")
    def choose_file(self, locator, file_path):
        """Inputs the ``file_path`` into the file input field ``locator``.

        This keyword is most often used to input files into upload forms.
        The keyword does not check ``file_path`` is the file or folder
        available on the machine where tests are executed. If the ``file_path``
        points at a file and when using Selenium Grid, Selenium will
        [https://seleniumhq.github.io/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.command.html?highlight=upload#selenium.webdriver.remote.command.Command.UPLOAD_FILE|magically],
        transfer the file from the machine where the tests are executed
        to the Selenium Grid node where the browser is running.
        Then Selenium will send the file path, from the nodes file
        system, to the browser.

        That ``file_path`` is not checked, is new in SeleniumLibrary 4.0.

        Example:
        | `Choose File` | my_upload_field | ${CURDIR}/trades.csv |
        """
        return self.formelementkeywords.choose_file(locator, file_path)

    @keyword(name="Input Password")
    def input_password(self, locator, password, clear=True):
        """Types the given password into the text field identified by ``locator``.

        See the `Locating elements` section for details about the locator
        syntax. See `Input Text` for ``clear`` argument details.

        Difference compared to `Input Text` is that this keyword does not
        log the given password on the INFO level. Notice that if you use
        the keyword like

        | Input Password | password_field | password |

        the password is shown as a normal keyword argument. A way to avoid
        that is using variables like

        | Input Password | password_field | ${PASSWORD} |

        Please notice that Robot Framework logs all arguments using
        the TRACE level and tests must not be executed using level below
        DEBUG if the password should not be logged in any format.

        The `clear` argument is new in SeleniumLibrary 4.0. Hiding password
        logging from Selenium logs is new in SeleniumLibrary 4.2.
        """
        return self.formelementkeywords.input_password(locator, password, clear)

    @keyword(name="Input Text")
    def input_text(self, locator, text, clear=True):
        """Types the given ``text`` into the text field identified by ``locator``.

        When ``clear`` is true, the input element is cleared before
        the text is typed into the element. When false, the previous text
        is not cleared from the element. Use `Input Password` if you
        do not want the given ``text`` to be logged.

        If [https://github.com/SeleniumHQ/selenium/wiki/Grid2|Selenium Grid]
        is used and the ``text`` argument points to a file in the file system,
        then this keyword prevents the Selenium to transfer the file to the
        Selenium Grid hub. Instead, this keyword will send the ``text`` string
        as is to the element. If a file should be transferred to the hub and
        upload should be performed, please use `Choose File` keyword.

        See the `Locating elements` section for details about the locator
        syntax. See the `Boolean arguments` section how Boolean values are
        handled.

        Disabling the file upload the Selenium Grid node and the `clear`
        argument are new in SeleniumLibrary 4.0
        """
        return self.formelementkeywords.input_text(locator, text, clear)

    @keyword(name="Page Should Contain Button")
    def page_should_contain_button(self, locator, message=None, loglevel='TRACE'):
        """Verifies button ``locator`` is found from current page.

        See `Page Should Contain Element` for an explanation about ``message``
        and ``loglevel`` arguments.

        See the `Locating elements` section for details about the locator
        syntax. When using the default locator strategy, buttons are
        searched using ``id``, ``name``, and ``value``.
        """
        return self.formelementkeywords.page_should_contain_button(locator, message, loglevel)

    @keyword(name="Page Should Contain Checkbox")
    def page_should_contain_checkbox(self, locator, message=None, loglevel='TRACE'):
        """Verifies checkbox ``locator`` is found from the current page.

        See `Page Should Contain Element` for an explanation about ``message``
        and ``loglevel`` arguments.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.formelementkeywords.page_should_contain_checkbox(locator, message, loglevel)

    @keyword(name="Page Should Contain Radio Button")
    def page_should_contain_radio_button(self, locator, message=None, loglevel='TRACE'):
        """Verifies radio button ``locator`` is found from current page.

        See `Page Should Contain Element` for an explanation about ``message``
        and ``loglevel`` arguments.

        See the `Locating elements` section for details about the locator
        syntax. When using the default locator strategy, radio buttons are
        searched using ``id``, ``name`` and ``value``.
        """
        return self.formelementkeywords.page_should_contain_radio_button(locator, message, loglevel)

    @keyword(name="Page Should Contain Textfield")
    def page_should_contain_textfield(self, locator, message=None, loglevel='TRACE'):
        """Verifies text field ``locator`` is found from current page.

        See `Page Should Contain Element` for an explanation about ``message``
        and ``loglevel`` arguments.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.formelementkeywords.page_should_contain_textfield(locator, message, loglevel)

    @keyword(name="Page Should Not Contain Button")
    def page_should_not_contain_button(self, locator, message=None, loglevel='TRACE'):
        """Verifies button ``locator`` is not found from current page.

        See `Page Should Contain Element` for an explanation about ``message``
        and ``loglevel`` arguments.

        See the `Locating elements` section for details about the locator
        syntax. When using the default locator strategy, buttons are
        searched using ``id``, ``name``, and ``value``.
        """
        return self.formelementkeywords.page_should_not_contain_button(locator, message, loglevel)

    @keyword(name="Page Should Not Contain Checkbox")
    def page_should_not_contain_checkbox(self, locator, message=None, loglevel='TRACE'):
        """Verifies checkbox ``locator`` is not found from the current page.

        See `Page Should Contain Element` for an explanation about ``message``
        and ``loglevel`` arguments.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.formelementkeywords.page_should_not_contain_checkbox(locator, message, loglevel)

    @keyword(name="Page Should Not Contain Radio Button")
    def page_should_not_contain_radio_button(self, locator, message=None, loglevel='TRACE'):
        """Verifies radio button ``locator`` is not found from current page.

        See `Page Should Contain Element` for an explanation about ``message``
        and ``loglevel`` arguments.

        See the `Locating elements` section for details about the locator
        syntax. When using the default locator strategy, radio buttons are
        searched using ``id``, ``name`` and ``value``.
        """
        return self.formelementkeywords.page_should_not_contain_radio_button(locator, message, loglevel)

    @keyword(name="Page Should Not Contain Textfield")
    def page_should_not_contain_textfield(self, locator, message=None, loglevel='TRACE'):
        """Verifies text field ``locator`` is not found from current page.

        See `Page Should Contain Element` for an explanation about ``message``
        and ``loglevel`` arguments.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.formelementkeywords.page_should_not_contain_textfield(locator, message, loglevel)

    @keyword(name="Radio Button Should Be Set To")
    def radio_button_should_be_set_to(self, group_name, value):
        """Verifies radio button group ``group_name`` is set to ``value``.

        ``group_name`` is the ``name`` of the radio button group.
        """
        return self.formelementkeywords.radio_button_should_be_set_to(group_name, value)

    @keyword(name="Radio Button Should Not Be Selected")
    def radio_button_should_not_be_selected(self, group_name):
        """Verifies radio button group ``group_name`` has no selection.

        ``group_name`` is the ``name`` of the radio button group.
        """
        return self.formelementkeywords.radio_button_should_not_be_selected(group_name)

    @keyword(name="Select Checkbox")
    def select_checkbox(self, locator):
        """Selects the checkbox identified by ``locator``.

        Does nothing if checkbox is already selected.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.formelementkeywords.select_checkbox(locator)

    @keyword(name="Select Radio Button")
    def select_radio_button(self, group_name, value):
        """Sets the radio button group ``group_name`` to ``value``.

        The radio button to be selected is located by two arguments:
        - ``group_name`` is the name of the radio button group.
        - ``value`` is the ``id`` or ``value`` attribute of the actual
          radio button.

        Examples:
        | `Select Radio Button` | size    | XL    |
        | `Select Radio Button` | contact | email |
        """
        return self.formelementkeywords.select_radio_button(group_name, value)

    @keyword(name="Submit Form")
    def submit_form(self, locator=None):
        """Submits a form identified by ``locator``.

        If ``locator`` is not given, first form on the page is submitted.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.formelementkeywords.submit_form(locator)

    @keyword(name="Textarea Should Contain")
    def textarea_should_contain(self, locator, expected, message=None):
        """Verifies text area ``locator`` contains text ``expected``.

        ``message`` can be used to override default error message.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.formelementkeywords.textarea_should_contain(locator, expected, message)

    @keyword(name="Textarea Value Should Be")
    def textarea_value_should_be(self, locator, expected, message=None):
        """Verifies text area ``locator`` has exactly text ``expected``.

        ``message`` can be used to override default error message.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.formelementkeywords.textarea_value_should_be(locator, expected, message)

    @keyword(name="Textfield Should Contain")
    def textfield_should_contain(self, locator, expected, message=None):
        """Verifies text field ``locator`` contains text ``expected``.

        ``message`` can be used to override the default error message.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.formelementkeywords.textfield_should_contain(locator, expected, message)

    @keyword(name="Textfield Value Should Be")
    def textfield_value_should_be(self, locator, expected, message=None):
        """Verifies text field ``locator`` has exactly text ``expected``.

        ``message`` can be used to override default error message.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.formelementkeywords.textfield_value_should_be(locator, expected, message)

    @keyword(name="Unselect Checkbox")
    def unselect_checkbox(self, locator):
        """Removes the selection of checkbox identified by ``locator``.

        Does nothing if the checkbox is not selected.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.formelementkeywords.unselect_checkbox(locator)

    @keyword(name="Current Frame Should Contain")
    def current_frame_should_contain(self, text, loglevel='TRACE'):
        """Verifies that the current frame contains ``text``.

        See `Page Should Contain` for an explanation about the ``loglevel``
        argument.

        Prior to SeleniumLibrary 3.0 this keyword was named
        `Current Frame Contains`.
        """
        return self.framekeywords.current_frame_should_contain(text, loglevel)

    @keyword(name="Current Frame Should Not Contain")
    def current_frame_should_not_contain(self, text, loglevel='TRACE'):
        """Verifies that the current frame does not contain ``text``.

        See `Page Should Contain` for an explanation about the ``loglevel``
        argument.
        """
        return self.framekeywords.current_frame_should_not_contain(text, loglevel)

    @keyword(name="Frame Should Contain")
    def frame_should_contain(self, locator, text, loglevel='TRACE'):
        """Verifies that frame identified by ``locator`` contains ``text``.

        See the `Locating elements` section for details about the locator
        syntax.

        See `Page Should Contain` for an explanation about the ``loglevel``
        argument.
        """
        return self.framekeywords.frame_should_contain(locator, text, loglevel)

    @keyword(name="Select Frame")
    def select_frame(self, locator):
        """Sets frame identified by ``locator`` as the current frame.

        See the `Locating elements` section for details about the locator
        syntax.

        Works both with frames and iframes. Use `Unselect Frame` to cancel
        the frame selection and return to the main frame.

        Example:
        | `Select Frame`   | top-frame | # Select frame with id or name 'top-frame'   |
        | `Click Link`     | example   | # Click link 'example' in the selected frame |
        | `Unselect Frame` |           | # Back to main frame.                        |
        | `Select Frame`   | //iframe[@name='xxx'] | # Select frame using xpath       |
        """
        return self.framekeywords.select_frame(locator)

    @keyword(name="Unselect Frame")
    def unselect_frame(self):
        """Sets the main frame as the current frame.

        In practice cancels the previous `Select Frame` call.
        """
        return self.framekeywords.unselect_frame()

    @keyword(name="Execute Async Javascript")
    def execute_async_javascript(self, *code):
        """Executes asynchronous JavaScript code with possible arguments.

        Similar to `Execute Javascript` except that scripts executed with
        this keyword must explicitly signal they are finished by invoking the
        provided callback. This callback is always injected into the executed
        function as the last argument.

        Scripts must complete within the script timeout or this keyword will
        fail. See the `Timeout` section for more information.

        Starting from SeleniumLibrary 3.2 it is possible to provide JavaScript
        [https://seleniumhq.github.io/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webdriver.html#selenium.webdriver.remote.webdriver.WebDriver.execute_async_script|
        arguments] as part of ``code`` argument. See `Execute Javascript` for
        more details.

        Examples:
        | `Execute Async JavaScript` | var callback = arguments[arguments.length - 1]; window.setTimeout(callback, 2000); |
        | `Execute Async JavaScript` | ${CURDIR}/async_js_to_execute.js |
        | ${result} = | `Execute Async JavaScript`                      |
        | ...         | var callback = arguments[arguments.length - 1]; |
        | ...         | function answer(){callback("text");};           |
        | ...         | window.setTimeout(answer, 2000);                |
        | `Should Be Equal` | ${result} | text |
        """
        return self.javascriptkeywords.execute_async_javascript(*code)

    @keyword(name="Execute Javascript")
    def execute_javascript(self, *code):
        """Executes the given JavaScript code with possible arguments.

        ``code`` may be divided into multiple cells in the test data and
        ``code`` may contain multiple lines of code and arguments. In that case,
        the JavaScript code parts are concatenated together without adding
        spaces and optional arguments are separated from ``code``.

        If ``code`` is a path to an existing file, the JavaScript
        to execute will be read from that file. Forward slashes work as
        a path separator on all operating systems.

        The JavaScript executes in the context of the currently selected
        frame or window as the body of an anonymous function. Use ``window``
        to refer to the window of your application and ``document`` to refer
        to the document object of the current frame or window, e.g.
        ``document.getElementById('example')``.

        This keyword returns whatever the executed JavaScript code returns.
        Return values are converted to the appropriate Python types.

        Starting from SeleniumLibrary 3.2 it is possible to provide JavaScript
        [https://seleniumhq.github.io/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webdriver.html#selenium.webdriver.remote.webdriver.WebDriver.execute_script|
        arguments] as part of ``code`` argument. The JavaScript code and
        arguments must be separated with `JAVASCRIPT` and `ARGUMENTS` markers
        and must be used exactly with this format. If the Javascript code is
        first, then the `JAVASCRIPT` marker is optional. The order of
        `JAVASCRIPT` and `ARGUMENTS` markers can be swapped, but if `ARGUMENTS`
        is the first marker, then `JAVASCRIPT` marker is mandatory. It is only
        allowed to use `JAVASCRIPT` and `ARGUMENTS` markers only one time in the
        ``code`` argument.

        Examples:
        | `Execute JavaScript` | window.myFunc('arg1', 'arg2') |
        | `Execute JavaScript` | ${CURDIR}/js_to_execute.js    |
        | `Execute JavaScript` | alert(arguments[0]); | ARGUMENTS | 123 |
        | `Execute JavaScript` | ARGUMENTS | 123 | JAVASCRIPT | alert(arguments[0]); |
        """
        return self.javascriptkeywords.execute_javascript(*code)

    @keyword(name="Register Keyword To Run On Failure")
    def register_keyword_to_run_on_failure(self, keyword):
        """Sets the keyword to execute, when a SeleniumLibrary keyword fails.

        ``keyword`` is the name of a keyword that will be executed if a
        SeleniumLibrary keyword fails. It is possible to use any available
        keyword, including user keywords or keywords from other libraries,
        but the keyword must not take any arguments.

        The initial keyword to use is set when `importing` the library, and
        the keyword that is used by default is `Capture Page Screenshot`.
        Taking a screenshot when something failed is a very useful
        feature, but notice that it can slow down the execution.

        It is possible to use string ``NOTHING`` or ``NONE``,
        case-insensitively, as well as Python ``None`` to disable this
        feature altogether.

        This keyword returns the name of the previously registered
        failure keyword or Python ``None`` if this functionality was
        previously disabled. The return value can be always used to
        restore the original value later.

        Example:
        | `Register Keyword To Run On Failure`  | Log Source |
        | ${previous kw}= | `Register Keyword To Run On Failure`  | NONE |
        | `Register Keyword To Run On Failure`  | ${previous kw} |

        Changes in SeleniumLibrary 3.0:
        - Possible to use string ``NONE`` or Python ``None`` to disable the
          functionality.
        - Return Python ``None`` when the functionality was disabled earlier.
          In previous versions special value ``No Keyword`` was returned and
          it could not be used to restore the original state.
        """
        return self.runonfailurekeywords.register_keyword_to_run_on_failure(keyword)

    @keyword(name="Capture Element Screenshot")
    def capture_element_screenshot(self, locator, filename='selenium-element-screenshot-{index}.png'):
        """Captures a screenshot from the element identified by ``locator`` and embeds it into log file.

        See `Capture Page Screenshot` for details about ``filename`` argument.
        See the `Locating elements` section for details about the locator
        syntax.

        An absolute path to the created element screenshot is returned.

        Support for capturing the screenshot from an element has limited support
        among browser vendors. Please check the browser vendor driver documentation
        does the browser support capturing a screenshot from an element.

        New in SeleniumLibrary 3.3. Support for EMBED is new in SeleniumLibrary 4.2.

        Examples:
        | `Capture Element Screenshot` | id:image_id |                                |
        | `Capture Element Screenshot` | id:image_id | ${OUTPUTDIR}/id_image_id-1.png |
        | `Capture Element Screenshot` | id:image_id | EMBED                          |
        """
        return self.screenshotkeywords.capture_element_screenshot(locator, filename)

    @keyword(name="Capture Page Screenshot")
    def capture_page_screenshot(self, filename='selenium-screenshot-{index}.png'):
        """Takes a screenshot of the current page and embeds it into a log file.

        ``filename`` argument specifies the name of the file to write the
        screenshot into. The directory where screenshots are saved can be
        set when `importing` the library or by using the `Set Screenshot
        Directory` keyword. If the directory is not configured, screenshots
        are saved to the same directory where Robot Framework's log file is
        written.

        If ``filename`` equals to EMBED (case insensitive), then screenshot
        is embedded as Base64 image to the log.html. In this case file is not
        created in the filesystem.

        Starting from SeleniumLibrary 1.8, if ``filename`` contains marker
        ``{index}``, it will be automatically replaced with an unique running
        index, preventing files to be overwritten. Indices start from 1,
        and how they are represented can be customized using Python's
        [https://docs.python.org/3/library/string.html#format-string-syntax|
        format string syntax].

        An absolute path to the created screenshot file is returned or if
        ``filename``  equals to EMBED, word `EMBED` is returned.

        Support for EMBED is new in SeleniumLibrary 4.2

        Examples:
        | `Capture Page Screenshot` |                                        |
        | `File Should Exist`       | ${OUTPUTDIR}/selenium-screenshot-1.png |
        | ${path} =                 | `Capture Page Screenshot`              |
        | `File Should Exist`       | ${OUTPUTDIR}/selenium-screenshot-2.png |
        | `File Should Exist`       | ${path}                                |
        | `Capture Page Screenshot` | custom_name.png                        |
        | `File Should Exist`       | ${OUTPUTDIR}/custom_name.png           |
        | `Capture Page Screenshot` | custom_with_index_{index}.png          |
        | `File Should Exist`       | ${OUTPUTDIR}/custom_with_index_1.png   |
        | `Capture Page Screenshot` | formatted_index_{index:03}.png         |
        | `File Should Exist`       | ${OUTPUTDIR}/formatted_index_001.png   |
        | `Capture Page Screenshot` | EMBED                                  |
        | `File Should Not Exist`   | EMBED                                  |
        """
        return self.screenshotkeywords.capture_page_screenshot(filename)

    @keyword(name="Set Screenshot Directory")
    def set_screenshot_directory(self, path):
        """Sets the directory for captured screenshots.

        ``path`` argument specifies the absolute path to a directory where
        the screenshots should be written to. If the directory does not
        exist, it will be created. The directory can also be set when
        `importing` the library. If it is not configured anywhere,
        screenshots are saved to the same directory where Robot Framework's
        log file is written.

        If ``path`` equals to EMBED (case insensitive) and
        `Capture Page Screenshot` or `capture Element Screenshot` keywords
        filename argument is not changed from the default value, then
        the page or element screenshot is embedded as Base64 image to
        the log.html.

        The previous value is returned and can be used to restore
        the original value later if needed.

        Returning the previous value is new in SeleniumLibrary 3.0.
        The persist argument was removed in SeleniumLibrary 3.2 and
        EMBED is new in SeleniumLibrary 4.2.
        """
        return self.screenshotkeywords.set_screenshot_directory(path)

    @keyword(name="Get List Items")
    def get_list_items(self, locator, values=False):
        """Returns all labels or values of selection list ``locator``.

        See the `Locating elements` section for details about the locator
        syntax.

        Returns visible labels by default, but values can be returned by
        setting the ``values`` argument to a true value (see `Boolean
        arguments`).

        Example:
        | ${labels} = | `Get List Items` | mylist              |             |
        | ${values} = | `Get List Items` | css:#example select | values=True |

        Support to return values is new in SeleniumLibrary 3.0.
        """
        return self.selectelementkeywords.get_list_items(locator, values)

    @keyword(name="Get Selected List Label")
    def get_selected_list_label(self, locator):
        """Returns the label of selected option from selection list ``locator``.

        If there are multiple selected options, the label of the first option
        is returned.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.selectelementkeywords.get_selected_list_label(locator)

    @keyword(name="Get Selected List Labels")
    def get_selected_list_labels(self, locator):
        """Returns labels of selected options from selection list ``locator``.

        Starting from SeleniumLibrary 3.0, returns an empty list if there
        are no selections. In earlier versions, this caused an error.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.selectelementkeywords.get_selected_list_labels(locator)

    @keyword(name="Get Selected List Value")
    def get_selected_list_value(self, locator):
        """Returns the value of selected option from selection list ``locator``.

        If there are multiple selected options, the value of the first option
        is returned.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.selectelementkeywords.get_selected_list_value(locator)

    @keyword(name="Get Selected List Values")
    def get_selected_list_values(self, locator):
        """Returns values of selected options from selection list ``locator``.

        Starting from SeleniumLibrary 3.0, returns an empty list if there
        are no selections. In earlier versions, this caused an error.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.selectelementkeywords.get_selected_list_values(locator)

    @keyword(name="List Selection Should Be")
    def list_selection_should_be(self, locator, *expected):
        """Verifies selection list ``locator`` has ``expected`` options selected.

        It is possible to give expected options both as visible labels and
        as values. Starting from SeleniumLibrary 3.0, mixing labels and
        values is not possible. Order of the selected options is not
        validated.

        If no expected options are given, validates that the list has
        no selections. A more explicit alternative is using `List Should
        Have No Selections`.

        See the `Locating elements` section for details about the locator
        syntax.

        Examples:
        | `List Selection Should Be` | gender    | Female          |        |
        | `List Selection Should Be` | interests | Test Automation | Python |
        """
        return self.selectelementkeywords.list_selection_should_be(locator, *expected)

    @keyword(name="List Should Have No Selections")
    def list_should_have_no_selections(self, locator):
        """Verifies selection list ``locator`` has no options selected.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.selectelementkeywords.list_should_have_no_selections(locator)

    @keyword(name="Page Should Contain List")
    def page_should_contain_list(self, locator, message=None, loglevel='TRACE'):
        """Verifies selection list ``locator`` is found from current page.

        See `Page Should Contain Element` for an explanation about ``message``
        and ``loglevel`` arguments.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.selectelementkeywords.page_should_contain_list(locator, message, loglevel)

    @keyword(name="Page Should Not Contain List")
    def page_should_not_contain_list(self, locator, message=None, loglevel='TRACE'):
        """Verifies selection list ``locator`` is not found from current page.

        See `Page Should Contain Element` for an explanation about ``message``
        and ``loglevel`` arguments.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.selectelementkeywords.page_should_not_contain_list(locator, message, loglevel)

    @keyword(name="Select All From List")
    def select_all_from_list(self, locator):
        """Selects all options from multi-selection list ``locator``.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.selectelementkeywords.select_all_from_list(locator)

    @keyword(name="Select From List By Index")
    def select_from_list_by_index(self, locator, *indexes):
        """Selects options from selection list ``locator`` by ``indexes``.

        Indexes of list options start from 0.

        If more than one option is given for a single-selection list,
        the last value will be selected. With multi-selection lists all
        specified options are selected, but possible old selections are
        not cleared.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.selectelementkeywords.select_from_list_by_index(locator, *indexes)

    @keyword(name="Select From List By Label")
    def select_from_list_by_label(self, locator, *labels):
        """Selects options from selection list ``locator`` by ``labels``.

        If more than one option is given for a single-selection list,
        the last value will be selected. With multi-selection lists all
        specified options are selected, but possible old selections are
        not cleared.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.selectelementkeywords.select_from_list_by_label(locator, *labels)

    @keyword(name="Select From List By Value")
    def select_from_list_by_value(self, locator, *values):
        """Selects options from selection list ``locator`` by ``values``.

        If more than one option is given for a single-selection list,
        the last value will be selected. With multi-selection lists all
        specified options are selected, but possible old selections are
        not cleared.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.selectelementkeywords.select_from_list_by_value(locator, *values)

    @keyword(name="Unselect All From List")
    def unselect_all_from_list(self, locator):
        """Unselects all options from multi-selection list ``locator``.

        See the `Locating elements` section for details about the locator
        syntax.

        New in SeleniumLibrary 3.0.
        """
        return self.selectelementkeywords.unselect_all_from_list(locator)

    @keyword(name="Unselect From List By Index")
    def unselect_from_list_by_index(self, locator, *indexes):
        """Unselects options from selection list ``locator`` by ``indexes``.

        Indexes of list options start from 0. This keyword works only with
        multi-selection lists.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.selectelementkeywords.unselect_from_list_by_index(locator, *indexes)

    @keyword(name="Unselect From List By Label")
    def unselect_from_list_by_label(self, locator, *labels):
        """Unselects options from selection list ``locator`` by ``labels``.

        This keyword works only with multi-selection lists.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.selectelementkeywords.unselect_from_list_by_label(locator, *labels)

    @keyword(name="Unselect From List By Value")
    def unselect_from_list_by_value(self, locator, *values):
        """Unselects options from selection list ``locator`` by ``values``.

        This keyword works only with multi-selection lists.

        See the `Locating elements` section for details about the locator
        syntax.
        """
        return self.selectelementkeywords.unselect_from_list_by_value(locator, *values)

    @keyword(name="Get Table Cell")
    def get_table_cell(self, locator, row, column, loglevel='TRACE'):
        """Returns contents of a table cell.

        The table is located using the ``locator`` argument and its cell
        found using ``row`` and ``column``. See the `Locating elements`
        section for details about the locator syntax.

        Both row and column indexes start from 1, and header and footer
        rows are included in the count. It is possible to refer to rows
        and columns from the end by using negative indexes so that -1
        is the last row/column, -2 is the second last, and so on.

        All ``<th>`` and ``<td>`` elements anywhere in the table are
        considered to be cells.

        See `Page Should Contain` for an explanation about the ``loglevel``
        argument.
        """
        return self.tableelementkeywords.get_table_cell(locator, row, column, loglevel)

    @keyword(name="Table Cell Should Contain")
    def table_cell_should_contain(self, locator, row, column, expected, loglevel='TRACE'):
        """Verifies table cell contains text ``expected``.

        See `Get Table Cell` that this keyword uses internally for
        an explanation about accepted arguments.
        """
        return self.tableelementkeywords.table_cell_should_contain(locator, row, column, expected, loglevel)

    @keyword(name="Table Column Should Contain")
    def table_column_should_contain(self, locator, column, expected, loglevel='TRACE'):
        """Verifies table column contains text ``expected``.

        The table is located using the ``locator`` argument and its column
        found using ``column``. See the `Locating elements` section for
        details about the locator syntax.

        Column indexes start from 1. It is possible to refer to columns
        from the end by using negative indexes so that -1 is the last column,
        -2 is the second last, and so on.

        If a table contains cells that span multiple columns, those merged
        cells count as a single column.

        See `Page Should Contain Element` for an explanation about the
        ``loglevel`` argument.
        """
        return self.tableelementkeywords.table_column_should_contain(locator, column, expected, loglevel)

    @keyword(name="Table Footer Should Contain")
    def table_footer_should_contain(self, locator, expected, loglevel='TRACE'):
        """Verifies table footer contains text ``expected``.

        Any ``<td>`` element inside ``<tfoot>`` element is considered to
        be part of the footer.

        The table is located using the ``locator`` argument. See the
        `Locating elements` section for details about the locator syntax.

        See `Page Should Contain Element` for an explanation about the
        ``loglevel`` argument.
        """
        return self.tableelementkeywords.table_footer_should_contain(locator, expected, loglevel)

    @keyword(name="Table Header Should Contain")
    def table_header_should_contain(self, locator, expected, loglevel='TRACE'):
        """Verifies table header contains text ``expected``.

        Any ``<th>`` element anywhere in the table is considered to be
        part of the header.

        The table is located using the ``locator`` argument. See the
        `Locating elements` section for details about the locator syntax.

        See `Page Should Contain Element` for an explanation about the
        ``loglevel`` argument.
        """
        return self.tableelementkeywords.table_header_should_contain(locator, expected, loglevel)

    @keyword(name="Table Row Should Contain")
    def table_row_should_contain(self, locator, row, expected, loglevel='TRACE'):
        """Verifies that table row contains text ``expected``.

        The table is located using the ``locator`` argument and its column
        found using ``column``. See the `Locating elements` section for
        details about the locator syntax.

        Row indexes start from 1. It is possible to refer to rows
        from the end by using negative indexes so that -1 is the last row,
        -2 is the second last, and so on.

        If a table contains cells that span multiple rows, a match
        only occurs for the uppermost row of those merged cells.

        See `Page Should Contain Element` for an explanation about the
        ``loglevel`` argument.
        """
        return self.tableelementkeywords.table_row_should_contain(locator, row, expected, loglevel)

    @keyword(name="Table Should Contain")
    def table_should_contain(self, locator, expected, loglevel='TRACE'):
        """Verifies table contains text ``expected``.

        The table is located using the ``locator`` argument. See the
        `Locating elements` section for details about the locator syntax.

        See `Page Should Contain Element` for an explanation about the
        ``loglevel`` argument.
        """
        return self.tableelementkeywords.table_should_contain(locator, expected, loglevel)

    @keyword(name="Wait For Condition")
    def wait_for_condition(self, condition, timeout=None, error=None):
        """Waits until ``condition`` is true or ``timeout`` expires.

        The condition can be arbitrary JavaScript expression but it
        must return a value to be evaluated. See `Execute JavaScript` for
        information about accessing content on pages.

        Fails if the timeout expires before the condition becomes true. See
        the `Timeouts` section for more information about using timeouts
        and their default value.

        ``error`` can be used to override the default error message.

        Examples:
        | `Wait For Condition` | return document.title == "New Title" |
        | `Wait For Condition` | return jQuery.active == 0            |
        | `Wait For Condition` | style = document.querySelector('h1').style; return style.background == "red" && style.color == "white" |
        """
        return self.waitingkeywords.wait_for_condition(condition, timeout, error)

    @keyword(name="Wait Until Element Contains")
    def wait_until_element_contains(self, locator, text, timeout=None, error=None):
        """Waits until the element ``locator`` contains ``text``.

        Fails if ``timeout`` expires before the text appears. See
        the `Timeouts` section for more information about using timeouts and
        their default value and the `Locating elements` section for details
        about the locator syntax.

        ``error`` can be used to override the default error message.
        """
        return self.waitingkeywords.wait_until_element_contains(locator, text, timeout, error)

    @keyword(name="Wait Until Element Does Not Contain")
    def wait_until_element_does_not_contain(self, locator, text, timeout=None, error=None):
        """Waits until the element ``locator`` does not contain ``text``.

        Fails if ``timeout`` expires before the text disappears. See
        the `Timeouts` section for more information about using timeouts and
        their default value and the `Locating elements` section for details
        about the locator syntax.

        ``error`` can be used to override the default error message.
        """
        return self.waitingkeywords.wait_until_element_does_not_contain(locator, text, timeout, error)

    @keyword(name="Wait Until Element Is Enabled")
    def wait_until_element_is_enabled(self, locator, timeout=None, error=None):
        """Waits until the element ``locator`` is enabled.

        Element is considered enabled if it is not disabled nor read-only.

        Fails if ``timeout`` expires before the element is enabled. See
        the `Timeouts` section for more information about using timeouts and
        their default value and the `Locating elements` section for details
        about the locator syntax.

        ``error`` can be used to override the default error message.

        Considering read-only elements to be disabled is a new feature
        in SeleniumLibrary 3.0.
        """
        return self.waitingkeywords.wait_until_element_is_enabled(locator, timeout, error)

    @keyword(name="Wait Until Element Is Not Visible")
    def wait_until_element_is_not_visible(self, locator, timeout=None, error=None):
        """Waits until the element ``locator`` is not visible.

        Fails if ``timeout`` expires before the element is not visible. See
        the `Timeouts` section for more information about using timeouts and
        their default value and the `Locating elements` section for details
        about the locator syntax.

        ``error`` can be used to override the default error message.
        """
        return self.waitingkeywords.wait_until_element_is_not_visible(locator, timeout, error)

    @keyword(name="Wait Until Element Is Visible")
    def wait_until_element_is_visible(self, locator, timeout=None, error=None):
        """Waits until the element ``locator`` is visible.

        Fails if ``timeout`` expires before the element is visible. See
        the `Timeouts` section for more information about using timeouts and
        their default value and the `Locating elements` section for details
        about the locator syntax.

        ``error`` can be used to override the default error message.
        """
        return self.waitingkeywords.wait_until_element_is_visible(locator, timeout, error)

    @keyword(name="Wait Until Location Contains")
    def wait_until_location_contains(self, expected, timeout=None, message=None):
        """Waits until the current URL contains ``expected``.

        The ``expected`` argument contains the expected value in url.

        Fails if ``timeout`` expires before the location contains. See
        the `Timeouts` section for more information about using timeouts
        and their default value.

        The ``message`` argument can be used to override the default error
        message.

        New in SeleniumLibrary 4.0
        """
        return self.waitingkeywords.wait_until_location_contains(expected, timeout, message)

    @keyword(name="Wait Until Location Does Not Contain")
    def wait_until_location_does_not_contain(self, location, timeout=None, message=None):
        """Waits until the current URL does not contains ``location``.

        The ``location`` argument contains value not expected in url.

        Fails if ``timeout`` expires before the location not contains. See
        the `Timeouts` section for more information about using timeouts
        and their default value.

        The ``message`` argument can be used to override the default error
        message.

        New in SeleniumLibrary 4.3
        """
        return self.waitingkeywords.wait_until_location_does_not_contain(location, timeout, message)

    @keyword(name="Wait Until Location Is")
    def wait_until_location_is(self, expected, timeout=None, message=None):
        """Waits until the current URL is ``expected``.

        The ``expected`` argument is the expected value in url.

        Fails if ``timeout`` expires before the location is. See
        the `Timeouts` section for more information about using timeouts
        and their default value.

        The ``message`` argument can be used to override the default error
        message.

        New in SeleniumLibrary 4.0
        """
        return self.waitingkeywords.wait_until_location_is(expected, timeout, message)

    @keyword(name="Wait Until Location Is Not")
    def wait_until_location_is_not(self, location, timeout=None, message=None):
        """Waits until the current URL is not ``location``.

        The ``location`` argument is the unexpected value in url.

        Fails if ``timeout`` expires before the location is not. See
        the `Timeouts` section for more information about using timeouts
        and their default value.

        The ``message`` argument can be used to override the default error
        message.

        New in SeleniumLibrary 4.3
        """
        return self.waitingkeywords.wait_until_location_is_not(location, timeout, message)

    @keyword(name="Wait Until Page Contains")
    def wait_until_page_contains(self, text, timeout=None, error=None):
        """Waits until ``text`` appears on the current page.

        Fails if ``timeout`` expires before the text appears. See
        the `Timeouts` section for more information about using timeouts
        and their default value.

        ``error`` can be used to override the default error message.
        """
        return self.waitingkeywords.wait_until_page_contains(text, timeout, error)

    @keyword(name="Wait Until Page Contains Element")
    def wait_until_page_contains_element(self, locator, timeout=None, error=None):
        """Waits until the element ``locator`` appears on the current page.

        Fails if ``timeout`` expires before the element appears. See
        the `Timeouts` section for more information about using timeouts and
        their default value and the `Locating elements` section for details
        about the locator syntax.

        ``error`` can be used to override the default error message.
        """
        return self.waitingkeywords.wait_until_page_contains_element(locator, timeout, error)

    @keyword(name="Wait Until Page Does Not Contain")
    def wait_until_page_does_not_contain(self, text, timeout=None, error=None):
        """Waits until ``text`` disappears from the current page.

        Fails if ``timeout`` expires before the text disappears. See
        the `Timeouts` section for more information about using timeouts
        and their default value.

        ``error`` can be used to override the default error message.
        """
        return self.waitingkeywords.wait_until_page_does_not_contain(text, timeout, error)

    @keyword(name="Wait Until Page Does Not Contain Element")
    def wait_until_page_does_not_contain_element(self, locator, timeout=None, error=None):
        """Waits until the element ``locator`` disappears from the current page.

        Fails if ``timeout`` expires before the element disappears. See
        the `Timeouts` section for more information about using timeouts and
        their default value and the `Locating elements` section for details
        about the locator syntax.

        ``error`` can be used to override the default error message.
        """
        return self.waitingkeywords.wait_until_page_does_not_contain_element(locator, timeout, error)

    @keyword(name="Close Window")
    def close_window(self):
        """Closes currently opened and selected browser window/tab. """
        return self.windowkeywords.close_window()

    @keyword(name="Get Locations")
    def get_locations(self, browser='CURRENT'):
        """Returns and logs URLs of all windows of the selected browser.

        *Browser Scope:*

        The ``browser`` argument specifies the browser that shall return
        its windows information.

        - ``browser`` can be ``index_or_alias`` like in `Switch Browser`.

        - If ``browser`` is ``CURRENT`` (default, case-insensitive)
          the currently active browser is selected.

        - If ``browser`` is ``ALL`` (case-insensitive)
          the window information of all windows of all opened browsers are returned."""
        return self.windowkeywords.get_locations(browser)

    @keyword(name="Get Window Handles")
    def get_window_handles(self, browser='CURRENT'):
        """Returns all child window handles of the selected browser as a list.

        Can be used as a list of windows to exclude with `Select Window`.

        How to select the ``browser`` scope of this keyword, see `Get Locations`.

        Prior to SeleniumLibrary 3.0, this keyword was named `List Windows`.
        """
        return self.windowkeywords.get_window_handles(browser)

    @keyword(name="Get Window Identifiers")
    def get_window_identifiers(self, browser='CURRENT'):
        """Returns and logs id attributes of all windows of the selected browser.

        How to select the ``browser`` scope of this keyword, see `Get Locations`."""
        return self.windowkeywords.get_window_identifiers(browser)

    @keyword(name="Get Window Names")
    def get_window_names(self, browser='CURRENT'):
        """Returns and logs names of all windows of the selected browser.

        How to select the ``browser`` scope of this keyword, see `Get Locations`."""
        return self.windowkeywords.get_window_names(browser)

    @keyword(name="Get Window Position")
    def get_window_position(self):
        """Returns current window position.

        The position is relative to the top left corner of the screen. Returned
        values are integers. See also `Set Window Position`.

        Example:
        | ${x} | ${y}= | `Get Window Position` |
        """
        return self.windowkeywords.get_window_position()

    @keyword(name="Get Window Size")
    def get_window_size(self, inner=False):
        """Returns current window width and height as integers.

        See also `Set Window Size`.

        If ``inner`` parameter is set to True, keyword returns
        HTML DOM window.innerWidth and window.innerHeight properties.
        See `Boolean arguments` for more details on how to set boolean
        arguments. The ``inner`` is new in SeleniumLibrary 4.0.

        Example:
        | ${width} | ${height}= | `Get Window Size` |      |
        | ${width} | ${height}= | `Get Window Size` | True |
        """
        return self.windowkeywords.get_window_size(inner)

    @keyword(name="Get Window Titles")
    def get_window_titles(self, browser='CURRENT'):
        """Returns and logs titles of all windows of the selected browser.

        How to select the ``browser`` scope of this keyword, see `Get Locations`."""
        return self.windowkeywords.get_window_titles(browser)

    @keyword(name="Maximize Browser Window")
    def maximize_browser_window(self):
        """Maximizes current browser window."""
        return self.windowkeywords.maximize_browser_window()

    @keyword(name="Select Window")
    def select_window(self, locator='MAIN', timeout=None):
        """DEPRECATED in SeleniumLibrary 4.0. , use `Switch Window` instead."""
        return self.windowkeywords.select_window(locator, timeout)

    @keyword(name="Set Window Position")
    def set_window_position(self, x, y):
        """Sets window position using ``x`` and ``y`` coordinates.

        The position is relative to the top left corner of the screen,
        but some browsers exclude possible task bar set by the operating
        system from the calculation. The actual position may thus be
        different with different browsers.

        Values can be given using strings containing numbers or by using
        actual numbers. See also `Get Window Position`.

        Example:
        | `Set Window Position` | 100 | 200 |
        """
        return self.windowkeywords.set_window_position(x, y)

    @keyword(name="Set Window Size")
    def set_window_size(self, width, height, inner=False):
        """Sets current windows size to given ``width`` and ``height``.

        Values can be given using strings containing numbers or by using
        actual numbers. See also `Get Window Size`.

        Browsers have a limit on their minimum size. Trying to set them
        smaller will cause the actual size to be bigger than the requested
        size.

        If ``inner`` parameter is set to True, keyword sets the necessary
        window width and height to have the desired HTML DOM _window.innerWidth_
        and _window.innerHeight_. See `Boolean arguments` for more details on how to set boolean
        arguments.

        The ``inner`` argument is new since SeleniumLibrary 4.0.

        This ``inner`` argument does not support Frames. If a frame is selected,
        switch to default before running this.

        Example:
        | `Set Window Size` | 800 | 600 |      |
        | `Set Window Size` | 800 | 600 | True |
        """
        return self.windowkeywords.set_window_size(width, height, inner)

    @keyword(name="Switch Window")
    def switch_window(self, locator='MAIN', timeout=None, browser='CURRENT'):
        """Switches to browser window matching ``locator``.

        If the window is found, all subsequent commands use the selected
        window, until this keyword is used again. If the window is not
        found, this keyword fails. The previous windows handle is returned
        and can be used to switch back to it later.

        Notice that alerts should be handled with
        `Handle Alert` or other alert related keywords.

        The ``locator`` can be specified using different strategies somewhat
        similarly as when `locating elements` on pages.

        - By default, the ``locator`` is matched against window handle, name,
          title, and URL. Matching is done in that order and the first
          matching window is selected.

        - The ``locator`` can specify an explicit strategy by using the format
          ``strategy:value`` (recommended) or ``strategy=value``. Supported
          strategies are ``name``, ``title``, and ``url``. These matches windows
          using their name, title, or URL, respectively. Additionally, ``default``
          can be used to explicitly use the default strategy explained above.

        - If the ``locator`` is ``NEW`` (case-insensitive), the latest
          opened window is selected. It is an error if this is the same
          as the current window.

        - If the ``locator`` is ``MAIN`` (default, case-insensitive),
          the main window is selected.

        - If the ``locator`` is ``CURRENT`` (case-insensitive), nothing is
          done. This effectively just returns the current window handle.

        - If the ``locator`` is not a string, it is expected to be a list
          of window handles _to exclude_. Such a list of excluded windows
          can be got from `Get Window Handles` before doing an action that
          opens a new window.

        The ``timeout`` is used to specify how long keyword will poll to select
        the new window. The ``timeout`` is new in SeleniumLibrary 3.2.

        Example:
        | `Click Link`      | popup1      |      | # Open new window |
        | `Switch Window`   | example     |      | # Select window using default strategy |
        | `Title Should Be` | Pop-up 1    |      |
        | `Click Button`    | popup2      |      | # Open another window |
        | ${handle} = | `Switch Window`   | NEW  | # Select latest opened window |
        | `Title Should Be` | Pop-up 2    |      |
        | `Switch Window`   | ${handle}   |      | # Select window using handle |
        | `Title Should Be` | Pop-up 1    |      |
        | `Switch Window`   | MAIN        |      | # Select the main window |
        | `Title Should Be` | Main        |      |
        | ${excludes} = | `Get Window Handles` | | # Get list of current windows |
        | `Click Link`      | popup3      |      | # Open one more window |
        | `Switch Window`   | ${excludes} |      | # Select window using excludes |
        | `Title Should Be` | Pop-up 3    |      |

        The ``browser`` argument allows with ``index_or_alias`` to implicitly switch to
        a specific browser when switching to a window. See `Switch Browser`

        - If the ``browser`` is ``CURRENT`` (case-insensitive), no other browser is
          selected.

        *NOTE:*

        - The ``strategy:value`` syntax is only supported by SeleniumLibrary
          3.0 and newer.
        - Prior to SeleniumLibrary 3.0 matching windows by name, title
          and URL was case-insensitive.
        - Earlier versions supported aliases ``None``, ``null`` and the
          empty string for selecting the main window, and alias ``self``
          for selecting the current window. Support for these aliases was
          removed in SeleniumLibrary 3.2.
        """
        return self.windowkeywords.switch_window(locator, timeout, browser)

