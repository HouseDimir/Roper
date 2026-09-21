from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.get("/")
def index():
  return render_template("_index.html")

@app.post("/generate")
def generate():
  print(request.form)
  is_exclusive = "is-exclusive" in request.form
  mode = request.form["mode"]
  is_rarity_balanced = "is-rarity-balanced" in request.form
  allow_gamechangers = "allow-gamechangers" in request.form
  cube_size = int(request.form["cube-size"])
  keywords = [x.strip() for x in request.form["keywords"].split()]
  set_codes = [x.strip() for x in request.form["set-codes"].split()]
  supertypes = [x.strip() for x in request.form["supertypes"].split()]
  subtypes = [x.strip() for x in request.form["subtypes"].split()]
  is_draft = "is-draft" in request.form
  draft_packs = int(request.form["draft-packs"])
  draft_cards_per_pack = int(request.form["draft-cards-per-pack"])

  print(f"is_exclusive = {is_exclusive}\nmode = {mode}\nis_rarity_balanced = {is_rarity_balanced}\nallow_gamechangers = {allow_gamechangers}\ncube_size = {cube_size}\nkeywords = {keywords}\nset_codes = {set_codes}\nsupertypes = {supertypes}\nsubtypes = {subtypes}\nis_draft = {is_draft}\ndraft_packs = {draft_packs}\ndraft_cards_per_pack = {draft_cards_per_pack}")
  return redirect(url_for("index"))
