![Edge](https://i.imgur.com/KbIYmhD.png)

`Edge` is a simple theme with bright colors. Edge comes in three versions — *Night Sky*, *Serene* and *Ocean* for all day long comfortable work. The theme has a few customisable options to help you personalise your experience with it.

## Installation

### Recommended

You can install `Edge` via [Package Control](https://packagecontrol.io/).

1. Press <kbd>cmd/ctrl</kbd> + <kbd>shift</kbd> + <kbd>p</kbd> to open the command palette.
2. Type `Install package` and press enter. Then search for `Edge`

### Manual

1. Download the [latest release](https://github.com/dempfi/ayu/releases/latest), extract and rename the directory to `Edge Theme`.
2. Move the directory inside your Sublime `/Packages` directory. *(Preferences > Browse packages...)*

## Activation

### Recommended

Open command palette via `Tools > Command Palette` (or <kbd>cmd/ctrl</kbd> + <kbd>shift</kbd> + <kbd>p</kbd>) and type `Edge: Activate theme`.

### With Skins package

[Skins](https://packagecontrol.io/packages/Skins) provides a simple and efficient way to change themes, save your own presets and quickly try out new looks. Activation is as simple as opening up the command palette, running `Select Skin` and choosing `Edge Night Sky`, `Edge Serene` or `Edge Ocean` from the list.

### Via Preferences

Add these lines to your user settings *Preferences > Setting - User*:

For the Night Sky theme:

```js
"theme": "Edge Night Sky.sublime-theme",
"color_scheme": "Packages/Edge Theme/Edge Night Sky.tmTheme",
```

For the Serene theme:

```js
"theme": "Edge Serene.sublime-theme",
"color_scheme": "Packages/Edge Theme/Edge Serene.tmTheme",
```

For the Ocean theme:

```js
"theme": "Edge Ocean.sublime-theme",
"color_scheme": "Packages/Edge Theme/Edge Ocean.tmTheme",
```

**NOTE:** Restart Sublime Text after activation of the theme to avoid any glitches.

## Settings

### Preferences

```
"edge_sidebar_font_small": false, // use a small font in the sidebar
"edge_sidebar_font_normal": false, // use a normal font in the sidebar
"edge_sidebar_font_large": false, // use a large font in the sidebar
"edge_sidebar_font_xlarge": false, // use an extra large font in the sidebar
"edge_use_sidebar_folder_icons": true, // use folder icons in the sidebar
"edge_use_font_face": true // use the custom font for the UI
```

### Font

`Edge` uses [__Hack__](http://sourcefoundry.org/hack/) as main font and it's highly recommended to install it to get a monospaced font in the filetree. But if you don't have it then the UI theme will downgrade to standard UI font used in Sublime Text. You can also disable it via `Edge Theme: Preferences`.

### File Icons

`Edge` is built from its initial release to support customization via [A File Icon](https://github.com/ihodev/a-file-icon) package. Please install it and restart Sublime for a better user expereince.

## Screenshots

**Edge Night Sky**

![Edge Night Sky](https://i.imgur.com/sxcgQd7.png)

**Edge Serene**

![Edge Serene](https://i.imgur.com/eCo70F2.png)

**Edge Ocean**

![Edge Ocean](https://i.imgur.com/MpXSHO2.png)

## Contributing to Edge

**Please check the CONTRIBUTING.md file before forking this repo!**
