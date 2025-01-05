from aiogram import Router, F, types

router = Router()


@router.message(F.text.in_(['Our branches 🏚', 'Наши филиалы 🏚', 'Filiallarimiz 🏚']))
async def branches_handler(message: types.Message):
    await message.answer_(
        "Here are the branches of the college:\n\n1. Computer Science and Engineering\n2. Electronics and Communication Engineering\n3. Mechanical Engineering\n4. Civil Engineering\n5. Electrical Engineering\n6. Industrial and Production Engineering\n7. Chemical Engineering\n8. Materials Science and Engineering\n9. Biomedical Engineering\n10. Agricultural Engineering\n11. Environmental Engineering\n12. Architecture and Planning\n13. Management Studies\n14. Economics and Business Administration\n15. Law and Legal Studies\n16. Psychology and Psychiatry\n17. Social Sciences and Humanities\n18. Nursing and Health Sciences\n19. Education and Training\n20. Public Policy and Administration\n21. International Studies\n22. Finance and Accounting\n23. Marketing and Communication\n24. Business Administration\n25. Humanities and Social Sciences\n26. Engineering Science and Technology\n27. Computer Science and Information Technology\n28. Mathematics and Statistics\n29. Physics and Astronomy\n30. Chemistry and Biochemistry\n31. Earth Sciences and Geology\n32. Life Sciences and Biology\n33. Other"
    )
