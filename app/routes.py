
from flask import Blueprint, render_template, session, redirect, url_for, request, flash

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('base.html')

@main.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    return render_template('dashboard.html')

# HTML Lessons
@main.route('/lessons/html-intro')
def html_intro():
    return render_template('lessons/html_intro.html')

@main.route('/lessons/html-editors')
def html_editors():
    return render_template('lessons/html_editors.html')

@main.route('/lessons/html-basic')
def html_basic():
    return render_template('lessons/html_basic.html')

@main.route('/lessons/html-elements')
def html_elements():
    return render_template('lessons/html_elements.html')

@main.route('/lessons/html-attributes')
def html_attributes():
    return render_template('lessons/html_attributes.html')

@main.route('/lessons/html-headings')
def html_headings():
    return render_template('lessons/html_headings.html')

@main.route('/lessons/html-paragraphs')
def html_paragraphs():
    return render_template('lessons/html_paragraphs.html')

@main.route('/lessons/html-styles')
def html_styles():
    return render_template('lessons/html_styles.html')

@main.route('/lessons/html-formatting')
def html_formatting():
    return render_template('lessons/html_formatting.html')

@main.route('/lessons/html-quotations')
def html_quotations():
    return render_template('lessons/html_quotations.html')

@main.route('/lessons/html-comments')
def html_comments():
    return render_template('lessons/html_comments.html')

@main.route('/lessons/html-colors')
def html_colors():
    return render_template('lessons/html_colors.html')

@main.route('/lessons/html-css')
def html_css():
    return render_template('lessons/html_css.html')

@main.route('/lessons/html-links')
def html_links():
    return render_template('lessons/html_links.html')

@main.route('/lessons/html-images')
def html_images():
    return render_template('lessons/html_images.html')

@main.route('/lessons/html-favicon')
def html_favicon():
    return render_template('lessons/html_favicon.html')

@main.route('/lessons/html-page-title')
def html_page_title():
    return render_template('lessons/html_page_title.html')

@main.route('/lessons/html-tables')
def html_tables():
    return render_template('lessons/html_tables.html')

@main.route('/lessons/html-lists')
def html_lists():
    return render_template('lessons/html_lists.html')

@main.route('/lessons/html-block-inline')
def html_block_inline():
    return render_template('lessons/html_block_inline.html')

@main.route('/lessons/html-div')
def html_div():
    return render_template('lessons/html_div.html')

@main.route('/lessons/html-classes')
def html_classes():
    return render_template('lessons/html_classes.html')

@main.route('/lessons/html-id')
def html_id():
    return render_template('lessons/html_id.html')

@main.route('/lessons/html-iframes')
def html_iframes():
    return render_template('lessons/html_iframes.html')

@main.route('/lessons/html-javascript')
def html_javascript():
    return render_template('lessons/html_javascript.html')

@main.route('/lessons/html-file-paths')
def html_file_paths():
    return render_template('lessons/html_file_paths.html')

@main.route('/lessons/html-head')
def html_head():
    return render_template('lessons/html_head.html')

@main.route('/lessons/html-layout')
def html_layout():
    return render_template('lessons/html_layout.html')

@main.route('/lessons/html-responsive')
def html_responsive():
    return render_template('lessons/html_responsive.html')

@main.route('/lessons/html-computercode')
def html_computercode():
    return render_template('lessons/html_computercode.html')

@main.route('/lessons/html-semantics')
def html_semantics():
    return render_template('lessons/html_semantics.html')

@main.route('/lessons/html-style-guide')
def html_style_guide():
    return render_template('lessons/html_style_guide.html')

# CSS Lessons
@main.route('/lessons/css-intro')
def css_intro():
    return render_template('lessons/css_intro.html')

# Python Lessons
@main.route('/lessons/python-intro')
def python_intro():
    return render_template('lessons/python_intro.html')

# HTML Exercises
@main.route('/exercises/html-quiz', methods=['GET', 'POST'])
def html_quiz():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        # Handle quiz submission
        score = 0
        total = 3
        
        # Check answers
        if request.form.get('q1') == 'a':
            score += 1
        if request.form.get('q2') == 'b':
            score += 1
        if request.form.get('q3') == 'b':
            score += 1
        
        flash(f'Quiz completed! You scored {score}/{total}')
        return redirect(url_for('main.html_quiz'))
    
    return render_template('exercises/html_quiz.html')

# CSS Exercises
@main.route('/exercises/css-quiz', methods=['GET', 'POST'])
def css_quiz():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        # Handle quiz submission
        score = 0
        total = 3
        
        # Check answers
        if request.form.get('q1') == 'a':
            score += 1
        if request.form.get('q2') == 'b':
            score += 1
        if request.form.get('q3') == 'b':
            score += 1
        
        flash(f'Quiz completed! You scored {score}/{total}')
        return redirect(url_for('main.css_quiz'))
    
    return render_template('exercises/css_quiz.html')

# Python Exercises
@main.route('/exercises/python-quiz', methods=['GET', 'POST'])
def python_quiz():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        # Handle quiz submission
        score = 0
        total = 3
        
        # Check answers
        if request.form.get('q1') == 'a':
            score += 1
        if request.form.get('q2') == 'b':
            score += 1
        if request.form.get('q3') == 'a':
            score += 1
        
        flash(f'Quiz completed! You scored {score}/{total}')
        return redirect(url_for('main.python_quiz'))
    
    return render_template('exercises/python_quiz.html')
