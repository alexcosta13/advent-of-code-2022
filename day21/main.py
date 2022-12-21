def compute(job_name, jobs):
    job = jobs[job_name]
    if isinstance(job, int):
        return job
    op = job[1]
    if op == "+":
        return compute(job[0], jobs) + compute(job[2], jobs)
    if op == "-":
        return compute(job[0], jobs) - compute(job[2], jobs)
    if op == "*":
        return compute(job[0], jobs) * compute(job[2], jobs)
    if op == "/":
        return compute(job[0], jobs) // compute(job[2], jobs)


def compute_inverse(const, op, res, humn_right=False):
    if op == "+":
        return res - const
    if op == "-":
        if humn_right:
            return const - res
        return res + const
    if op == "*":
        return res // const
    if op == "/":
        if humn_right:
            return const // res
        return res * const


def has_humn(job_name, jobs):
    if job_name == "humn":
        return True
    job = jobs[job_name]
    if isinstance(job, int):
        return False
    return has_humn(job[0], jobs) or has_humn(job[2], jobs)


def want_result(job_name, result, jobs):
    left, operation, right = jobs[job_name]

    if left == "humn":
        return compute_inverse(compute(right, jobs), operation, result)
    if right == "humn":
        return compute_inverse(compute(left, jobs), operation, result, True)

    if has_humn(left, jobs):
        return want_result(
            left, compute_inverse(compute(right, jobs), operation, result), jobs
        )
    if has_humn(right, jobs):
        return want_result(
            right, compute_inverse(compute(left, jobs), operation, result, True), jobs
        )

    raise NotImplementedError()


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()
    jobs = {
        job.split(": ")[0]: job.split(": ")[1].split()
        if len(job.split(": ")[1].split()) > 1
        else int(job.split(": ")[1])
        for job in lines.split("\n")
    }

    part1 = compute("root", jobs)
    print("First part:", part1)

    jobs["root"][1] = "-"
    part2 = want_result("root", 0, jobs)
    print("Second part:", part2)
