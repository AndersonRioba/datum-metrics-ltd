document.addEventListener('DOMContentLoaded', () => {
  function attachCKEditor() {
    const targetFields = document.querySelectorAll(
      'textarea#id_content, textarea#id_description, textarea#id_challenge, textarea#id_solution, textarea#id_results'
    );

    targetFields.forEach((el) => {
      if (el.dataset.ckeditorAttached) return;
      el.dataset.ckeditorAttached = 'true';

      window.ClassicEditor
        .create(el, {
          toolbar: [
            'heading', '|',
            'bold', 'italic', 'link', 'bulletedList', 'numberedList', 'blockQuote', '|',
            'insertTable', 'undo', 'redo', 'code', 'codeBlock'
          ],
        })
        .then(editor => {
          editor.editing.view.change(writer => {
            writer.setStyle('min-height', '260px', editor.editing.view.document.getRoot());
          });
        })
        .catch(error => {
          console.error('CKEditor init error:', error);
        });
    });
  }

  if (!window.ClassicEditor) {
    const script = document.createElement('script');
    script.src = 'https://cdn.ckeditor.com/ckeditor5/41.1.0/classic/ckeditor.js';
    script.onload = () => attachCKEditor();
    document.head.appendChild(script);
  } else {
    attachCKEditor();
  }
});
