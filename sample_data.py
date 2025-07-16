# Sample data for Question Answering with Transformers

sample_english = [
    {
        "id": "1",
        "context": "Welcome to ShopEase, your one-stop online store for electronics, clothing, and home essentials. We offer free shipping on orders over $50 and a 30-day return policy. Our customer support is available 24/7 to assist you with any inquiries. You can track your order status in your account dashboard. For exclusive deals, sign up for our newsletter.",
        "question": "What is the minimum order amount for free shipping?",
        "recommended_questions": [
            "What is the minimum order amount for free shipping?",
            "How can I track my order status?"
        ],
        "answers": [
            {"text": "$50", "answer_start": 86},
            {"text": "in your account dashboard", "answer_start": 207}
        ]
    },
    {
        "id": "2",
        "context": "The Theory of Evolution, first formulated by Charles Darwin in his book 'On the Origin of Species', explains how species evolve over time through the process of natural selection. Organisms with traits better suited to their environment tend to survive and reproduce, passing those advantageous traits to their offspring. This gradual process results in the diversity of life seen on Earth today.",
        "question": "Who formulated the Theory of Evolution?",
        "recommended_questions": [
            "Who formulated the Theory of Evolution?",
            "What is the main mechanism behind the Theory of Evolution?"
        ],
        "answers": [
            {"text": "Charles Darwin", "answer_start": 38},
            {"text": "natural selection", "answer_start": 120}
        ]
    },
    {
        "id": "3",
        "context": "Renewable energy sources such as solar, wind, hydroelectric, and geothermal power are critical to reducing greenhouse gas emissions and combating climate change. Unlike fossil fuels, renewable energy sources are naturally replenished and offer sustainable alternatives for electricity generation. Many countries are investing heavily in renewable technologies to transition to a cleaner energy future.",
        "question": "Name two renewable energy sources mentioned.",
        "recommended_questions": [
            "Name two renewable energy sources mentioned.",
            "Why are renewable energy sources important for combating climate change?"
        ],
        "answers": [
            {"text": "solar, wind", "answer_start": 24},
            {"text": "they are critical to reducing greenhouse gas emissions and combating climate change", "answer_start": 74}
        ]
    }
]

sample_arabic = [
    {
        "id": "ar1",
        "context": "القاهرة هي عاصمة جمهورية مصر العربية وأكبر مدنها من حيث عدد السكان، حيث يبلغ عدد سكانها أكثر من 20 مليون نسمة. تقع القاهرة على ضفاف نهر النيل في شمال مصر، وتعتبر مركزاً سياسياً واقتصادياً وثقافياً مهماً في المنطقة العربية. تأسست القاهرة في عام 969 ميلادية على يد جوهر الصقلي قائد جيوش المعز لدين الله الفاطمي، وأصبحت عاصمة للدولة الفاطمية. تتميز القاهرة بوجود العديد من المعالم التاريخية مثل الأهرامات وأبو الهول والقلعة والمساجد التاريخية، كما أنها مركز مهم للتعليم والبحث العلمي في مصر والمنطقة العربية.",
        "question": "ما هي عاصمة مصر؟",
        "recommended_questions": [
            "ما هي عاصمة مصر؟",
            "ما هي بعض المعالم التاريخية في القاهرة؟"
        ],
        "answers": [
            {"text": "القاهرة", "answer_start": 0},
            {"text": "الأهرامات وأبو الهول والقلعة والمساجد التاريخية", "answer_start": 252}
        ]
    },
    {
        "id": "ar2",
        "context": "ولد أحمد زويل في مدينة دمنهور المصرية في 26 فبراير 1946، وهو عالم كيميائي مصري أمريكي حصل على جائزة نوبل في الكيمياء عام 1999 لعمله في مجال كيمياء الفيمتو. درس زويل في جامعة الإسكندرية وحصل على بكالوريوس العلوم في الكيمياء، ثم سافر إلى الولايات المتحدة الأمريكية لإكمال دراسته العليا. عمل زويل في معهد كاليفورنيا للتكنولوجيا (كالتك) وأصبح أستاذاً للكيمياء والفيزياء. اكتشف زويل تقنية الفيمتو ثانية التي تسمح بمراقبة التفاعلات الكيميائية في أسرع وقت ممكن، مما أحدث ثورة في مجال الكيمياء والفيزياء.",
        "question": "في أي مدينة وُلد أحمد زويل؟",
        "recommended_questions": [
            "في أي مدينة وُلد أحمد زويل؟",
            "ما هو الإنجاز العلمي الذي حصل بسببه أحمد زويل على جائزة نوبل؟"
        ],
        "answers": [
            {"text": "دمنهور", "answer_start": 21},
            {"text": "تقنية الفيمتو ثانية", "answer_start": 357}
        ]
    },
    {
        "id": "ar3",
        "context": "جامعة الأزهر هي واحدة من أقدم الجامعات في العالم، تأسست في القاهرة عام 970 ميلادية على يد جوهر الصقلي في عهد الدولة الفاطمية. بدأت الجامعة كمدرسة لتعليم العلوم الإسلامية واللغة العربية، ثم تطورت لتصبح جامعة شاملة تدرس مختلف العلوم الإنسانية والطبيعية. يقع الحرم الجامعي الرئيسي في حي الأزهر بالقاهرة، وتضم الجامعة العديد من الكليات والمعاهد في مختلف محافظات مصر. تعتبر جامعة الأزهر من أهم مراكز التعليم الإسلامي في العالم، وتخرج منها العديد من العلماء والمفكرين على مر التاريخ.",
        "question": "متى تأسست جامعة الأزهر؟",
        "recommended_questions": [
            "متى تأسست جامعة الأزهر؟",
            "ما هو الدور الذي تلعبه جامعة الأزهر في التعليم الإسلامي؟"
        ],
        "answers": [
            {"text": "970 ميلادية", "answer_start": 89},
            {"text": "من أهم مراكز التعليم الإسلامي في العالم", "answer_start": 357}
        ]
    }
] 