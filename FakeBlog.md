<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My Best Restaurants in SFLa Blog!</title>
    <meta name="description" content="This blog features all of the best restaurants
    in the South Florida Area">
    <link rel="stylesheet" href="css_file.css">
    <script src="jslib.js"></script>
  </head>

  <body>
    <div>
      <p>Lorem ipsum dolor <span id="bold">sit amet, consectetur adipiscing elit. Integer tempor dictum ante nec scelerisque.
      Suspendisse est quam, ornare at imperdiet sed, fringilla vel diam</span>. Aliquam quis sodales enim. Suspendisse
      potenti. Donec id molestie diam, nec pharetra enim. Aliquam ante dui,eleifend lacinia erat nec, aliquet finibus
      ipsum. In accumsan bibendum blandit. Nullam non erat sed dui.</p>

      <p><a href="www.google.com">Click for restaurant's website</a></p>

      <h4>Best So Far</h4>
        <ul>
          <li>Ipsum</li>
          <li>Dolorum</li>
          <li>Tedium</li>
        </ul>


      <table>
        <thead>
          <tr>
            <th>Restaurant</th>
            <th>Website</th>
            <th>Phone</th>
        </thead>
        <tbody>
          <tr>
            <td>MaiKai</td>
            <td>maikai@gmail</td>
            <td>954679395</td>
          </tr>
        </tbody>
      </table>

      <h5>Do the survey</h5>
        <form action="process.php" method="post">
            <p>Take the survey!</p>
            <label>
            Name:<input type="text" name="name">
            </label>

            <p>Dude or Gal</p>
            <label>
              <input type="radio" name="gender" value="dude">Dude
            </label>
              <label>
              <input type="radio" name="gender" value="gal">Gal
           </label>

           <p>Fave type of food</p>
            <label>
              <input type="checkbox" name="food" value="thai">Thai
            </label>
            <label>
              <input type="checkbox" name="food" value="italian">Italian
            </label>
            <label>
              <input type="checkbox" name="food" value="french">French
            </label>

            <p>Where do you live</p>
              <select name="county">
                <option value="broward">Broward</option>
                <option value="dade">Dade</option>
                </select>
            <input type="submit" value="submit">
          </form>
        </div>
    </body>
</html>
