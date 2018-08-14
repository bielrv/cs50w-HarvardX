// Import main SCSS for webpack compilation
import './styles/main.scss'

// Import all JS lib for webpack compilation
import './scripts/lib'

// Import your custom function
import { type, navActivePage, movingBackgroundImage } from './scripts/main'

// Import all assets for webpack compilation
function importAll(r) {
  return r.keys().map(r)
}
importAll(require.context('./assets', true, /\.(png|jpe?g|svg)$/))

// Declare which function are accessible to the browser
Object.assign(window, {
  type, navActivePage, movingBackgroundImage
})
