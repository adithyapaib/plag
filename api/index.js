const axios = require('axios');
const express = require('express');
const app = express();
const cors = require('cors');

// Middle Wares
app.use(express.json());
app.use(cors({origin: '*'}));

// Routes
// send the index.html file
app.get('/', (req, res) => res.sendFile(__dirname + '/index.html'));

app.post('/', async (req, res) => {
  const { data } = await req.body;
  console.log(data);

  // Request Headers
  const burp0_url = process.env.burp0_url;
  const burp0_cookies = {
    "PHPSESSID": process.env.PHPSESSID,
    "first_interaction_user": process.env.first_interaction_user,
    "first_interaction_order": process.env.first_interaction_order,
    "affiliate_user": process.env.affiliate_user,
    "sbjs_migrations": process.env.sbjs_migrations,
    "sbjs_current_add": process.env.sbjs_current_add,
    "sbjs_first_add": process.env.sbjs_first_add,
    "sbjs_current": process.env.sbjs_current,
    "sbjs_first": process.env.sbjs_first,
    "sbjs_udata": process.env.sbjs_udata,
    "sbjs_session": process.env.sbjs_session,
    "_ga_788D7MTZB4": process.env.ga_788D7MTZB4,
    "_ga": process.env.ga,
    "trustedsite_visit": process.env.trustedsite_visit,
    "trustedsite_tm_float_seen": process.env.trustedsite_tm_float_seen,
    "AppleBannercookie_hide_header_banner": process.env.AppleBannercookie_hide_header_banner,
    "COOKIE_PLAGIARISM_CHECKER_TERMS": process.env.COOKIE_PLAGIARISM_CHECKER_TERMS,
    "plagiarism_checker_progress_state": process.env.plagiarism_checker_progress_state
  };
  const burp0_headers = { "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0", "Accept": "/", "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": process.env.Referer, "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": process.env.Origin, "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "no-cors", "Sec-Fetch-Site": "same-origin", "Pragma": "no-cache", "Cache-Control": "no-cache", "Te": "trailers", "Connection": "close" };
  const burp0_data = {"is_free": "false","plagchecker_locale": "en","product_paper_type": "1","title": '',"text": String(data),};

  // Fetching Data
  try {
    const { data } = await axios.post(burp0_url, burp0_data, { headers: burp0_headers,cookies: burp0_cookies });
    console.log(data);
    return res.status(200).send(data);
  } catch (error) {
    console.log(error);
    return res.status(500).send({ message: 'Internal Server Error'});
  }
});

export default app;